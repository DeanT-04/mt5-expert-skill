import os

# Base Directories
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOCS_DIR = os.path.join(PROJECT_ROOT, "docs")
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
SCRIPTS_DIR = os.path.join(PROJECT_ROOT, "scripts")
TESTS_DIR = os.path.join(PROJECT_ROOT, "tests")

# Single Source of Truth for Skill Resources
SKILL_DIR = os.path.join(PROJECT_ROOT, ".agents", "skills", "mt5-expert")
REFERENCES_DIR = os.path.join(SKILL_DIR, "references")
TEMPLATES_DIR = os.path.join(SKILL_DIR, "templates")

# File Paths
PDF_PATH = os.path.join(DOCS_DIR, "mql5.pdf")
DB_PATH = os.path.join(DATA_DIR, "mql5_index.db")
SYMBOL_MAP_PATH = os.path.join(DATA_DIR, "symbol_map.json")

# MT5 Terminal & MetaEditor Configuration
METAEDITOR_PATH = r"C:\Program Files\BlackBull Markets MT5\MetaEditor64.exe"
DEFAULT_TERMINAL_BASE = r"C:\Users\Deano\AppData\Roaming\MetaQuotes\Terminal\16D9C17040576AD13C62C316983027D5\MQL5"
EXPERTS_DIR = os.path.join(DEFAULT_TERMINAL_BASE, "Experts")
INDICATORS_DIR = os.path.join(DEFAULT_TERMINAL_BASE, "Indicators")

def ensure_directories():
    """Ensure all required project directories exist."""
    os.makedirs(DOCS_DIR, exist_ok=True)
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(REFERENCES_DIR, exist_ok=True)
    os.makedirs(TEMPLATES_DIR, exist_ok=True)
    os.makedirs(EXPERTS_DIR, exist_ok=True)
    os.makedirs(INDICATORS_DIR, exist_ok=True)
