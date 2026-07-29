# High-Performance MT5 Expert v2 Stress Test Runner for PowerShell
Set-Location $PSScriptRoot

uv run python scripts/stress_test_cli.py $args
