import pytest
import sqlite3
import json
import os
from scripts.search.symbol_table import load_symbol_map, lookup_symbol
from scripts.search.fts_search import search_fts_database
from scripts.search.engine import query_dual_layer

def test_load_symbol_map(tmp_path):
    map_file = tmp_path / "symbol_map.json"
    map_file.write_text(json.dumps({"CTrade": {"type": "class"}}))
    
    data = load_symbol_map(str(map_file))
    assert "CTrade" in data
    
    non_existent = load_symbol_map("non_existent.json")
    assert non_existent == {}

def test_lookup_symbol():
    data = {"OrderSend": {"type": "function"}, "OnnxCreate": {"type": "function"}}
    
    # Test default fallback
    default_res = lookup_symbol("OrderSend")
    assert isinstance(default_res, dict)
    
    exact = lookup_symbol("OrderSend", symbol_map=data)
    assert "OrderSend" in exact
    
    partial = lookup_symbol("Onnx", symbol_map=data)
    assert "OnnxCreate" in partial

def test_search_fts_database(tmp_path):
    assert search_fts_database("query", db_path="non_existent.db") == []
    
    db_file = tmp_path / "mql5_index.db"
    conn = sqlite3.connect(str(db_file))
    cursor = conn.cursor()
    cursor.execute("CREATE VIRTUAL TABLE mql5_fts USING fts5(page_number, title, snippet);")
    cursor.execute("INSERT INTO mql5_fts VALUES (1, 'CTrade Class', 'CTrade handles order placing');")
    conn.commit()
    conn.close()
    
    results = search_fts_database("CTrade", db_path=str(db_file))
    assert len(results) == 1
    assert results[0]["title"] == "CTrade Class"
    
    # Test invalid query exception fallback
    assert search_fts_database("NOT ( syntax error", db_path=str(db_file)) == []

def test_query_dual_layer(tmp_path):
    map_file = tmp_path / "symbol_map.json"
    map_file.write_text(json.dumps({"iRSI": {"type": "function"}}))
    
    db_file = tmp_path / "mql5_index.db"
    conn = sqlite3.connect(str(db_file))
    cursor = conn.cursor()
    cursor.execute("CREATE VIRTUAL TABLE mql5_fts USING fts5(page_number, title, snippet);")
    cursor.execute("INSERT INTO mql5_fts VALUES (10, 'RSI Oscillator', 'iRSI calculates strength');")
    conn.commit()
    conn.close()
    
    res = query_dual_layer("iRSI", db_path=str(db_file), symbol_map_path=str(map_file))
    assert res["query"] == "iRSI"
    assert "iRSI" in res["symbol_table_matches"]
    assert len(res["pdf_snippets"]) == 1
