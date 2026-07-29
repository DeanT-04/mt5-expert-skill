import pytest
import os
import sys
import platform
from unittest.mock import patch, MagicMock
from scripts.utils.hardware_detector import detect_cpu_specs, detect_gpu_specs, auto_detect_hardware

def test_detect_cpu_specs_real():
    specs = detect_cpu_specs()
    assert "name" in specs
    assert specs["physical_cores"] >= 1
    assert specs["logical_cpus"] >= 1

@patch("subprocess.run")
def test_detect_cpu_specs_mocked_json(mock_sub):
    mock_res = MagicMock()
    mock_res.returncode = 0
    mock_res.stdout = '{"Name": "Mocked CPU", "NumberOfCores": 8, "NumberOfLogicalProcessors": 16}'
    mock_sub.return_value = mock_res
    
    with patch("platform.system", return_value="Windows"):
        specs = detect_cpu_specs()
        assert specs["name"] == "Mocked CPU"
        assert specs["physical_cores"] == 8
        assert specs["logical_cpus"] == 16

@patch("subprocess.run")
def test_detect_gpu_specs_mocked_json(mock_sub):
    mock_res = MagicMock()
    mock_res.returncode = 0
    mock_res.stdout = '[{"Name": "NVIDIA GeForce RTX 4090"}]'
    mock_sub.return_value = mock_res
    
    with patch("platform.system", return_value="Windows"):
        gpus = detect_gpu_specs()
        assert "NVIDIA GeForce RTX 4090" in gpus

def test_auto_detect_hardware_variations():
    hw = auto_detect_hardware()
    assert "cpu_name" in hw
    assert "gpus" in hw
    assert hw["optimal_threads"] >= 1

@patch("scripts.utils.hardware_detector.detect_cpu_specs")
def test_auto_detect_hardware_high_core_count(mock_cpu):
    mock_cpu.return_value = {"name": "Threadripper", "physical_cores": 32, "logical_cpus": 64}
    hw = auto_detect_hardware()
    assert hw["optimal_threads"] == 32

@patch("subprocess.run")
def test_hardware_exception_fallbacks(mock_sub):
    mock_sub.side_effect = Exception("Subprocess fail")
    cpu = detect_cpu_specs()
    gpu = detect_gpu_specs()
    assert cpu["logical_cpus"] >= 1
    assert len(gpu) >= 1

def test_hardware_detector_main_entry():
    import scripts.utils.hardware_detector as hw_mod
    with patch("builtins.print"):
        hw_mod.auto_detect_hardware()
