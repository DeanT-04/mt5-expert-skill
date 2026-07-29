import sqlite3
import os
from scripts.config import DB_PATH, DATA_DIR
from scripts.indexer.pdf_parser import parse_pdf_document

def init_fts_database(db_file=DB_PATH):
    """Initialize SQLite FTS5 table structure."""
    os.makedirs(os.path.dirname(db_file), exist_ok=True)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS mql5_fts;")
    cursor.execute("""
        CREATE VIRTUAL TABLE mql5_fts USING fts5(
            page_number UNINDEXED,
            title,
            snippet
        );
    """)
    conn.commit()
    conn.close()

def build_fts_database(pdf_file, db_file=DB_PATH, max_pages=None, batch_size=500):
    """Build SQLite FTS5 database from PDF document."""
    init_fts_database(db_file)
    
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    batch = []
    count = 0
    
    for item in parse_pdf_document(pdf_file, max_pages=max_pages):
        if item["text"]:
            batch.append((item["page_number"], item["title"], item["text"]))
            count += 1
            
        if len(batch) >= batch_size:
            cursor.executemany("INSERT INTO mql5_fts VALUES (?, ?, ?);", batch)
            conn.commit()
            batch = []
            
    if batch:
        cursor.executemany("INSERT INTO mql5_fts VALUES (?, ?, ?);", batch)
        conn.commit()
        
    conn.close()
    return count
