import json
import os
import re
from scripts.config import SYMBOL_MAP_PATH

def load_symbol_map(path=SYMBOL_MAP_PATH):
    """Load symbol_map.json into memory."""
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def lookup_symbol(query, symbol_map=None):
    """Instant (< 1ms) symbol table lookup for natural language or raw symbols."""
    if symbol_map is None:
        symbol_map = load_symbol_map()
        
    q = query.strip()
    if q in symbol_map:
        return {q: symbol_map[q]}
        
    # Extract identifiers from query string (e.g. "iRSI", "CTrade", "OrderSend")
    tokens = re.findall(r'\b[A-Za-z0-9_]+\b', query)
    matches = {}
    
    for token in tokens:
        if token in symbol_map:
            matches[token] = symbol_map[token]
        else:
            for k, v in symbol_map.items():
                if token.lower() in k.lower() and len(token) >= 3:
                    matches[k] = v
                    
    return matches
