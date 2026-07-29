import pytest
import os
from unittest.mock import patch, MagicMock
from scripts.stress_test_cli import generate_500_prompts, execute_single_query, run_stress_test, export_report

def test_generate_500_prompts():
    dataset = generate_500_prompts()
    assert len(dataset) == 500
    assert dataset[0][0] == 1
    assert "EURUSD" in dataset[0][1]

def test_execute_single_query():
    res = execute_single_query((1, "OnnxCreate model inference"))
    assert res["id"] == 1
    assert res["success"] is True
    assert res["symbol"] == "OnnxCreate"

def test_run_stress_test_mini(tmp_path):
    res = run_stress_test(num_queries=10, num_threads=2, verbose=False)
    assert res["num_queries"] == 10
    
    target_report = tmp_path / "test_report.md"
    rep_path = export_report(str(target_report))
    assert os.path.exists(rep_path)
