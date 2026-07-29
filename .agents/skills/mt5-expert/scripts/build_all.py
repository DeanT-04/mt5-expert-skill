import os
import sys
import time

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.config import PDF_PATH, DB_PATH, SYMBOL_MAP_PATH, ensure_directories
from scripts.indexer.symbol_extractor import generate_symbol_map
from scripts.indexer.db_builder import build_fts_database

def build_project_indexes():
    """Run full index build pipeline on docs/mql5.pdf."""
    print("=" * 60)
    print("MT5 EXPERT v2 - DUAL-LAYER INDEX BUILDER")
    print("=" * 60)
    
    ensure_directories()
    
    start_time = time.time()
    
    # 1. Generate Symbol Map
    print(f"\n[1/2] Generating Symbol Map at: {SYMBOL_MAP_PATH}")
    sym_count = generate_symbol_map(SYMBOL_MAP_PATH)
    print(f"      Mapped {sym_count} core MQL5 symbols.")
    
    # 2. Build SQLite FTS5 Database
    print(f"\n[2/2] Indexing PDF document from: {PDF_PATH}")
    if not os.path.exists(PDF_PATH):
        print(f"      ERROR: PDF file not found at: {PDF_PATH}")
        sys.exit(1)
        
    page_count = build_fts_database(PDF_PATH, DB_PATH)
    print(f"      Indexed {page_count} pages into FTS5 SQLite DB at: {DB_PATH}")
    
    elapsed = time.time() - start_time
    print(f"\nBUILD COMPLETE! Total execution time: {elapsed:.2f} seconds.")
    print("=" * 60)

if __name__ == "__main__":
    build_project_indexes()
