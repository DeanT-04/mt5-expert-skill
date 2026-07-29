import sqlite3
import os
import re
from scripts.config import DB_PATH

STOPWORDS = {"how", "to", "use", "in", "the", "a", "an", "and", "or", "for", "with", "of", "on", "using", "function", "parameters", "signature", "how", "what", "is", "can", "i", "mql5", "mt5"}

def clean_query_tokens(query):
    """Extract key identifiers and terms from natural language query for FTS5."""
    tokens = re.findall(r'\b[A-Za-z0-9_]+\b', query)
    keywords = [t for t in tokens if t.lower() not in STOPWORDS]
    
    if not keywords:
        return query
        
    # Join keywords with OR operator for FTS5 flexibility
    fts_query = " OR ".join(keywords[:5])
    return fts_query

def search_fts_database(query, db_path=DB_PATH, limit=5):
    """SQLite FTS5 full-text snippet query engine (< 3ms)."""
    if not os.path.exists(db_path):
        return []
        
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    clean_q = clean_query_tokens(query)
    
    try:
        cursor.execute(
            "SELECT page_number, title, snippet FROM mql5_fts WHERE mql5_fts MATCH ? ORDER BY rank LIMIT ?;",
            (clean_q, limit)
        )
        rows = cursor.fetchall()
        return [{"page": r[0], "title": r[1], "snippet": r[2]} for r in rows]
    except Exception:
        # Fallback to simple query if FTS expression error
        try:
            tokens = re.findall(r'\b[A-Za-z0-9_]{3,}\b', query)
            if tokens:
                single_kw = tokens[0]
                cursor.execute(
                    "SELECT page_number, title, snippet FROM mql5_fts WHERE mql5_fts MATCH ? ORDER BY rank LIMIT ?;",
                    (single_kw, limit)
                )
                rows = cursor.fetchall()
                return [{"page": r[0], "title": r[1], "snippet": r[2]} for r in rows]
        except Exception:
            pass
        return []
    finally:
        conn.close()
