@echo off
REM High-Performance MT5 Expert v2 Stress Test Runner for Windows

cd /d "%~dp0"
uv run python scripts\stress_test_cli.py %*
