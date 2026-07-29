import os
from scripts import config

def test_config_paths():
    assert os.path.exists(config.PROJECT_ROOT)
    assert config.PDF_PATH.endswith("mql5.pdf")
    assert config.DB_PATH.endswith("mql5_index.db")
    assert config.SYMBOL_MAP_PATH.endswith("symbol_map.json")

def test_ensure_directories(tmp_path):
    config.ensure_directories()
    assert os.path.exists(config.DOCS_DIR)
    assert os.path.exists(config.DATA_DIR)
