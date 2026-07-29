import pytest
import os
from unittest.mock import patch, MagicMock
from scripts.compiler.repair_engine import auto_repair_code, compile_with_auto_repair
from scripts.build_all import build_project_indexes

def test_auto_repair_code_missing_include():
    code = "CTrade trade;\nint OnInit() { return 0; }"
    repaired = auto_repair_code(code, ["error: 'trade' - struct / class undefined"], [])
    assert "#include <Trade\\Trade.mqh>" in repaired

def test_auto_repair_code_missing_return():
    code = "int OnInit() { return; }"
    repaired = auto_repair_code(code, ["error: not all control paths return a value"], [])
    assert "return(INIT_SUCCEEDED);" in repaired

def test_auto_repair_code_no_change():
    code = "#include <Trade\\Trade.mqh>\nCTrade trade;\nint OnInit() { return(INIT_SUCCEEDED); }"
    repaired = auto_repair_code(code, [], [])
    assert repaired == code

@patch("scripts.compiler.repair_engine.deploy_and_compile_mql5")
def test_compile_with_auto_repair_success(mock_deploy, tmp_path):
    mock_deploy.return_value = {
        "success": True,
        "errors": [],
        "warnings": [],
        "target_path": str(tmp_path / "test.mq5")
    }
    
    res = compile_with_auto_repair(str(tmp_path / "test.mq5"))
    assert res["success"] is True
    assert res["retries"] == 0

@patch("scripts.compiler.repair_engine.deploy_and_compile_mql5")
def test_compile_with_auto_repair_loop(mock_deploy, tmp_path):
    target = tmp_path / "test.mq5"
    target.write_text("CTrade trade;")
    
    # First attempt fails, second succeeds
    mock_deploy.side_effect = [
        {"success": False, "errors": ["'trade' - struct / class undefined"], "warnings": [], "target_path": str(target)},
        {"success": True, "errors": [], "warnings": [], "target_path": str(target)}
    ]
    
    res = compile_with_auto_repair(str(target), max_retries=2)
    assert res["success"] is True
    assert res["retries"] == 1

@patch("scripts.build_all.build_fts_database")
@patch("scripts.build_all.generate_symbol_map")
def test_build_project_indexes_mocked(mock_sym, mock_db):
    mock_sym.return_value = 24
    mock_db.return_value = 100
    build_project_indexes()
    assert mock_sym.called
    assert mock_db.called
