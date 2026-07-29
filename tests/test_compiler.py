import pytest
import os
from unittest.mock import patch, MagicMock
from scripts.compiler.log_parser import parse_metaeditor_log
from scripts.compiler.executor import run_metaeditor_compiler
from scripts.compiler.deployer import deploy_and_compile_mql5

def test_parse_metaeditor_log():
    log = """
    test.mq5(10,5) : error 123: 'foo' - undeclared identifier
    test.mq5(12,1) : warning 400: implicit conversion
    """
    errs, warns = parse_metaeditor_log(log)
    assert len(errs) == 1
    assert len(warns) == 1

def test_run_metaeditor_compiler_missing_exe(tmp_path):
    with pytest.raises(FileNotFoundError):
        run_metaeditor_compiler(str(tmp_path / "dummy.mq5"), metaeditor_exe="fake.exe")

def test_run_metaeditor_compiler_missing_mq5(tmp_path):
    existing_exe = r"C:\Program Files\BlackBull Markets MT5\MetaEditor64.exe"
    with pytest.raises(FileNotFoundError):
        run_metaeditor_compiler(str(tmp_path / "non_existent.mq5"), metaeditor_exe=existing_exe)

def test_deploy_and_compile_invalid_type(tmp_path):
    source = tmp_path / "dummy.mq5"
    source.write_text("// dummy")
    with pytest.raises(ValueError):
        deploy_and_compile_mql5(str(source), target_type="invalid_type", terminal_base=str(tmp_path))

def test_deploy_and_compile_valid_ea(tmp_path):
    source = tmp_path / "valid_ea.mq5"
    source.write_text("""
    #property copyright "2026"
    int OnInit() { return 0; }
    void OnTick() {}
    """)
    term_dir = tmp_path / "terminal"
    metaeditor_exe = r"C:\Program Files\BlackBull Markets MT5\MetaEditor64.exe"
    
    res = deploy_and_compile_mql5(
        str(source),
        target_type="strategy",
        custom_name="custom_ea.mq5",
        terminal_base=str(term_dir),
        metaeditor_exe=metaeditor_exe
    )
    
    assert res["success"] is True
    assert os.path.exists(res["target_path"])
    assert res["ex5_path"] is not None
    assert os.path.exists(res["ex5_path"])
