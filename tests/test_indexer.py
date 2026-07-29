import pytest
import os
import sqlite3
import json
from unittest.mock import patch, MagicMock
from scripts.indexer.pdf_parser import parse_pdf_document, extract_page_text
from scripts.indexer.db_builder import init_fts_database, build_fts_database
from scripts.indexer.symbol_extractor import generate_symbol_map

def test_extract_page_text():
    mock_page = MagicMock()
    mock_page.extract_text.return_value = " Hello \n World! "
    text = extract_page_text(mock_page)
    assert text == "Hello World!"

def test_extract_page_text_exception():
    mock_page = MagicMock()
    mock_page.extract_text.side_effect = Exception("Extract error")
    text = extract_page_text(mock_page)
    assert text == ""

def test_parse_pdf_document_missing_file():
    with pytest.raises(FileNotFoundError):
        list(parse_pdf_document(pdf_file="non_existent.pdf"))

@patch("pypdf.PdfReader")
def test_parse_pdf_document_mocked(mock_reader_cls, tmp_path):
    fake_pdf = tmp_path / "fake.pdf"
    fake_pdf.write_text("pdf content")
    
    mock_page = MagicMock()
    mock_page.extract_text.return_value = "Page text sample."
    
    mock_instance = MagicMock()
    mock_instance.pages = [mock_page, mock_page]
    mock_reader_cls.return_value = mock_instance
    
    results = list(parse_pdf_document(pdf_file=str(fake_pdf), max_pages=2))
    assert len(results) == 2
    assert results[0]["title"] == "Page text sample"

@patch("scripts.indexer.db_builder.parse_pdf_document")
def test_build_fts_database_mocked(mock_parse, tmp_path):
    mock_parse.return_value = [
        {"page_number": 1, "title": "Intro", "text": "Welcome to MQL5"},
        {"page_number": 2, "title": "Trade", "text": "CTrade handles orders"},
        {"page_number": 3, "title": "Empty", "text": ""}
    ]
    db_file = tmp_path / "test_mql5_index.db"
    
    count = build_fts_database(pdf_file="dummy.pdf", db_file=str(db_file), batch_size=1)
    assert count == 2
    assert os.path.exists(str(db_file))
    
    conn = sqlite3.connect(str(db_file))
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM mql5_fts;")
    total = cursor.fetchone()[0]
    conn.close()
    assert total == 2

def test_generate_symbol_map(tmp_path):
    target_json = tmp_path / "symbol_map.json"
    count = generate_symbol_map(output_path=str(target_json))
    assert count > 10
    assert os.path.exists(str(target_json))
    
    with open(str(target_json), 'r') as f:
        data = json.load(f)
    assert "CTrade" in data
    assert "iRSI" in data
