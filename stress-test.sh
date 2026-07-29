#!/usr/bin/env bash
# High-Performance MT5 Expert v2 Stress Test Runner

cd "$(dirname "$0")" || exit 1

echo "==========================================================================="
echo " 🔥 RUNNING MT5 EXPERT v2 STRESS TEST CLI"
echo "==========================================================================="

uv run python scripts/stress_test_cli.py "$@"
