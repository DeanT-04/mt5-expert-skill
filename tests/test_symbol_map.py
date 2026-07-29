import pytest
import json
import sqlite3
import os
from scripts.search.symbol_table import load_symbol_map, lookup_symbol
from scripts.search.fts_search import search_fts_database
from scripts.search.engine import query_dual_layer

def test_load_symbol_map(tmp_path):
    map_file = tmp_path / "symbol_map.json"
    dummy_data = {"OrderSend": {"signature": "bool OrderSend(...)"}}
    map_file.write_text(json.dumps(dummy_data))
    
    result = load_symbol_map(str(map_file))
    assert "OrderSend" in result

def test_load_symbol_map_non_existent():
    result = load_symbol_map("non_existent_file.json")
    assert result == {}

def test_load_symbol_map_default():
    res = load_symbol_map()
    assert isinstance(res, dict)

def test_search_symbol_exact_and_partial():
    data = {
        "OrderSend": {"signature": "bool OrderSend(...)"},
        "OnnxCreate": {"signature": "long OnnxCreate(...)"}
    }
    exact = lookup_symbol("OrderSend", symbol_map=data)
    assert exact == {"OrderSend": {"signature": "bool OrderSend(...)"}}
    
    partial = lookup_symbol("Onnx", symbol_map=data)
    assert "OnnxCreate" in partial
    
    none_match = lookup_symbol("NonExistentSymbol", symbol_map=data)
    assert none_match == {}

def test_search_symbol_default_map():
    res = lookup_symbol("OrderSend")
    assert isinstance(res, dict)

def test_search_fts5_db(tmp_path):
    db_file = tmp_path / "mql5_index.db"
    conn = sqlite3.connect(str(db_file))
    cursor = conn.cursor()
    cursor.execute("CREATE VIRTUAL TABLE mql5_fts USING fts5(page_number, title, snippet);")
    cursor.execute("INSERT INTO mql5_fts VALUES (100, 'ONNX Support', 'OnnxCreate creates a model handle');")
    conn.commit()
    conn.close()
    
    res = search_fts_database("ONNX", db_path=str(db_file))
    assert len(res) == 1
    assert res[0]["page"] == 100
    assert "OnnxCreate" in res[0]["snippet"]

def test_search_fts5_db_non_existent():
    res = search_fts_database("query", db_path="non_existent.db")
    assert res == []

def test_search_fts5_db_exception(tmp_path):
    invalid_db = tmp_path / "invalid.db"
    invalid_db.write_text("not a sqlite db")
    res = search_fts_database("query", db_path=str(invalid_db))
    assert res == []

def test_dual_layer_lookup(tmp_path):
    map_file = tmp_path / "symbol_map.json"
    dummy_map = {"iRSI": {"signature": "int iRSI(...)"}}
    map_file.write_text(json.dumps(dummy_map))
    
    db_file = tmp_path / "mql5_index.db"
    conn = sqlite3.connect(str(db_file))
    cursor = conn.cursor()
    cursor.execute("CREATE VIRTUAL TABLE mql5_fts USING fts5(page_number, title, snippet);")
    cursor.execute("INSERT INTO mql5_fts VALUES (50, 'RSI Indicator', 'iRSI calculates RSI oscillator');")
    conn.commit()
    conn.close()
    
    res = query_dual_layer("iRSI", db_path=str(db_file), symbol_map_path=str(map_file))
    assert res["query"] == "iRSI"
    assert "iRSI" in res["symbol_table_matches"]
    assert len(res["pdf_snippets"]) == 1
