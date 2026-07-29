from scripts.search.symbol_table import lookup_symbol, load_symbol_map
from scripts.search.fts_search import search_fts_database
from scripts.config import DB_PATH, SYMBOL_MAP_PATH

def query_dual_layer(query, db_path=DB_PATH, symbol_map_path=SYMBOL_MAP_PATH, limit=5):
    """Combines Layer 1 (Symbol Table) and Layer 2 (FTS5 DB) for split-second retrieval."""
    sym_map = load_symbol_map(symbol_map_path)
    symbols = lookup_symbol(query, symbol_map=sym_map)
    snippets = search_fts_database(query, db_path=db_path, limit=limit)
    
    return {
        "query": query,
        "symbol_table_matches": symbols,
        "pdf_snippets": snippets
    }
