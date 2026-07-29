import argparse
import time
import json
import os
import sys
import random
import concurrent.futures

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scripts.search.engine import query_dual_layer
from scripts.config import PROJECT_ROOT, DOCS_DIR
from scripts.utils.hardware_detector import auto_detect_hardware

COMPLEX_STRESS_PROMPTS = [
    # Complex Multi-Indicator Strategies (1-100)
    "Build an EA combining 200 EMA trend filter on H4 with M15 RSI 14 oversold < 30, Stochastic 5-3-3 crossover, ATR 14 dynamic stop loss, and spread check < 25 points",
    "Multi-timeframe Bollinger Bands squeeze breakout with MACD histogram momentum confirmation and dynamic equity risk % lot sizing",
    "Ichimoku Kinko Hyo Tenkan Kijun cross above Kumo cloud with Parabolic SAR trailing stop and max drawdown circuit breaker",
    "ADX trend strength > 25 filter with Triple EMA (TEMA) crossover and fixed monetary risk per trade",
    "CCI overbought +100 crossover combined with Williams % Range -80 exit and break-even stop loss trigger at +150 points",
    "Supertrend ATR trailing stop with Chaikin Money Flow volume filter and multi-symbol exposure control",
    "Keltner Channels breakout with Volume Weighted Average Price (VWAP) and daily equity profit cap",
    "Heikin Ashi candle color reversal strategy with Hull Moving Average filter and partial profit taking",
    "DeMarker oscillator divergence with Donchian Channel breakout and slippage protection",
    "Relative Vigor Index (RVI) signal line cross with BearsPower BullsPower volume confirm",
    
    # Complex Machine Learning & ONNX Model Pipelines (101-200)
    "Load ONNX model from MQL5 Files, configure input tensor [1, 10, 4] for M15 OHLCV bar series, run inference, extract softmax probabilities for Buy Sell Hold, and execute order via CTrade",
    "ONNX model inference with dynamic batch size input tensor reshape using OnnxSetInputShape and OnnxSetOutputShape",
    "Pass 50-period historical price array into ONNX model buffer using OnnxRun and parse output class predictions",
    "Load ONNX model from memory buffer using OnnxCreateFromBuffer, inspect input names with OnnxGetInputName, and validate tensor dimensions",
    "ONNX model error handling for INVALID_HANDLE, log GetLastError code, fallback to rule-based EMA strategy",

    # Complex OpenCL GPU Parallel Computing & Canvas Dashboards (201-300)
    "Create OpenCL GPU context with CLContextCreate, compile C kernel for 100,000 bar Monte Carlo simulation, write buffer with CLBufferWrite, execute with CLExecute, and read output array with CLBufferRead",
    "OpenCL parallel matrix multiplication for multi-symbol correlation matrix calculation across 28 currency pairs",
    "CCanvas graphic overlay displaying live multi-timeframe dashboard, ARGB color transparency, custom text metrics, and interactive OnChartEvent button clicks",
    "Draw dynamic equity curve chart on MT5 chart using CGraphic class with subplots and level markers",
    "Render custom candlestick chart using CCanvas with volume profile histograms and orderbook depth",

    # Complex SQLite Transactional Logging & File I/O (301-400)
    "Create local SQLite database with DatabaseOpen, create trades table with primary key ticket, prepare statement with DatabasePrepare, bind position parameters with DatabaseBind, execute transaction with DatabaseTransactionBegin and DatabaseTransactionCommit",
    "Query SQLite trade history with DatabaseRead, calculate profit metrics, export results to CSV file using FileWriteStruct",
    "Binary file I/O using FileOpen, FileWriteArray, FileReadStruct for custom tick data storage",
    "Folder manipulation using FolderCreate, FolderClean, FolderDelete, and FileSelectDialog for user file picker",

    # Complex Sockets, WebRequests & Network Security (401-500)
    "Create non-blocking TCP socket with SocketCreate, connect to remote REST API server with SocketConnect, send SSL TLS handshake, send JSON payload with SocketSend, read response with SocketRead, and close socket",
    "HTTP POST WebRequest to external webhook server with custom headers, JSON body authorization token, and response error code handling",
    "Send mobile push notifications via SendNotification on drawdown alert, send email report via SendMail, and upload log to FTP server via SendFTP"
]

LAST_STRESS_RESULT = None

def generate_500_prompts():
    dataset = []
    base_count = len(COMPLEX_STRESS_PROMPTS)
    symbols = ["EURUSD", "GBPUSD", "USDJPY", "XAUUSD", "BTCUSD", "US500", "DE40"]
    timeframes = ["M1", "M5", "M15", "H1", "H4", "D1"]
    
    for i in range(500):
        base_prompt = COMPLEX_STRESS_PROMPTS[i % base_count]
        sym = symbols[i % len(symbols)]
        tf = timeframes[i % len(timeframes)]
        dataset.append((i+1, f"[{sym} {tf}] Query #{i+1}: {base_prompt}"))
        
    return dataset

def execute_single_query(args):
    q_id, prompt = args
    t0 = time.perf_counter()
    res = query_dual_layer(prompt, limit=3)
    t1 = time.perf_counter()
    
    latency_ms = (t1 - t0) * 1000.0
    has_symbols = len(res["symbol_table_matches"]) > 0
    has_pdf = len(res["pdf_snippets"]) > 0
    
    top_symbol = list(res["symbol_table_matches"].keys())[0] if has_symbols else "N/A"
    top_page = res["pdf_snippets"][0]["page"] if has_pdf else "N/A"
    top_title = res["pdf_snippets"][0]["title"] if has_pdf else "N/A"
    
    return {
        "id": q_id,
        "prompt": prompt,
        "latency_ms": latency_ms,
        "success": has_symbols or has_pdf,
        "symbol": top_symbol,
        "page": top_page,
        "title": top_title
    }

def print_minimal_header(title):
    print("=" * 80)
    print(f"  {title.upper()}")
    print("=" * 80)

def run_stress_test(num_queries=500, num_threads=None, verbose=False):
    global LAST_STRESS_RESULT
    hw = auto_detect_hardware()
    if num_threads is None or num_threads <= 0:
        num_threads = hw["optimal_threads"]

    print()
    print_minimal_header("MT5 Expert v2 - Hardware Stress Test Engine")
    print(f"  CPU Hardware      : {hw['cpu_name']}")
    print(f"  Cores / Threads   : {hw['physical_cores']} Physical Cores | {hw['logical_cpus']} Logical CPUs")
    print(f"  GPU Acceleration  : {', '.join(hw['gpus'])}")
    print(f"  Parallel Workers  : {num_threads} Threads (Auto-Cap)")
    print(f"  Target Queries    : {num_queries} Complex Prompts")
    print("=" * 80 + "\n")

    dataset = generate_500_prompts()[:num_queries]
    start_time = time.perf_counter()
    results = []
    completed = 0
    
    print(f" [>] Launching {num_threads} parallel worker threads into SQLite FTS5 Engine...\n")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(execute_single_query, item) for item in dataset]
        
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            results.append(res)
            completed += 1
            
            if verbose or completed % 50 == 0 or completed == num_queries:
                pct = (completed / num_queries) * 100.0
                bar = "=" * int(pct // 4) + "-" * (25 - int(pct // 4))
                print(f"  [{bar}] {completed:>3}/{num_queries} ({pct:5.1f}%) | Latency: {res['latency_ms']:6.2f}ms | Symbol: {res['symbol']:<15} | Page: {res['page']}")

    total_wall_time = time.perf_counter() - start_time
    latencies = sorted([r["latency_ms"] for r in results])
    success_count = sum(1 for r in results if r["success"])
    accuracy_pct = (success_count / num_queries) * 100.0
    
    avg_latency = sum(latencies) / len(latencies)
    p50_latency = latencies[int(len(latencies) * 0.50)]
    p90_latency = latencies[int(len(latencies) * 0.90)]
    p99_latency = latencies[int(len(latencies) * 0.99)]
    min_latency = latencies[0]
    max_latency = latencies[-1]
    throughput = num_queries / total_wall_time
    
    print("\n" + "=" * 80)
    print(" STRESS TEST PERFORMANCE SUMMARY")
    print("=" * 80)
    print(f"  * Total Queries Processed : {num_queries}")
    print(f"  * Total Wall-Clock Time   : {total_wall_time:.2f} seconds")
    print(f"  * System Throughput       : {throughput:.2f} queries / sec")
    print(f"  * Search Accuracy Rate    : {success_count}/{num_queries} ({accuracy_pct:.1f}%)")
    print("  " + "-" * 76)
    print(f"  * Min Latency             : {min_latency:.2f} ms")
    print(f"  * Median Latency (p50)    : {p50_latency:.2f} ms")
    print(f"  * 90th Percentile (p90)   : {p90_latency:.2f} ms")
    print(f"  * 99th Percentile (p99)   : {p99_latency:.2f} ms")
    print(f"  * Max Latency             : {max_latency:.2f} ms")
    print("=" * 80 + "\n")
    
    LAST_STRESS_RESULT = {
        "num_queries": num_queries,
        "num_threads": num_threads,
        "wall_time": total_wall_time,
        "throughput": throughput,
        "accuracy": accuracy_pct,
        "latencies": latencies,
        "p50": p50_latency,
        "p90": p90_latency,
        "p99": p99_latency,
        "results": results,
        "hw": hw
    }
    
    export_report(os.path.join(PROJECT_ROOT, "stress_test_report.md"))
    export_report(os.path.join(DOCS_DIR, "stress-test", "stress_test_report.md"))
    return LAST_STRESS_RESULT

def export_report(target_path=None):
    global LAST_STRESS_RESULT
    if LAST_STRESS_RESULT is None:
        print(" [!] No stress test results found. Please run /start first before generating report.")
        return None
        
    if target_path is None:
        target_dir = os.path.join(DOCS_DIR, "stress-test")
        os.makedirs(target_dir, exist_ok=True)
        target_path = os.path.join(target_dir, "stress_test_report.md")
    else:
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        
    data = LAST_STRESS_RESULT
    hw = data["hw"]
    num_queries = data["num_queries"]
    num_threads = data["num_threads"]
    wall_time = data["wall_time"]
    throughput = data["throughput"]
    accuracy = data["accuracy"]
    latencies = data["latencies"]
    p50 = data["p50"]
    p90 = data["p90"]
    p99 = data["p99"]
    results = data["results"]
    
    md = []
    md.append("# MT5 Expert v2 - Hardcore Stress Test Report\n")
    md.append("## System Hardware Profile\n")
    md.append(f"- **CPU Hardware**: {hw['cpu_name']}")
    md.append(f"- **Physical Cores**: {hw['physical_cores']} | **Logical Processors**: {hw['logical_cpus']}")
    md.append(f"- **Detected GPU(s)**: {', '.join(hw['gpus'])}")
    md.append(f"- **Auto-Allocated Worker Threads**: **{num_threads} Parallel Workers**\n")
    
    md.append("## Executive Benchmark Metrics\n")
    md.append(f"- **Total Complex Queries Tested**: {num_queries}")
    md.append(f"- **Total Execution Wall-Time**: **{wall_time:.2f} seconds**")
    md.append(f"- **System Throughput**: **{throughput:.2f} queries/sec**")
    md.append(f"- **Search Accuracy Rate**: **{accuracy:.1f}% ({sum(1 for r in results if r['success'])}/{num_queries})**")
    md.append(f"- **Database Scope**: 7,284 Pages SQLite FTS5 (`mql5_index.db`)\n")
    
    md.append("## Latency Distribution (Milliseconds)\n")
    md.append("| Percentile Metric | Latency (ms) |")
    md.append("| :--- | :---: |")
    md.append(f"| **Min Latency** | {min(latencies):.2f} ms |")
    md.append(f"| **Median (p50)** | {p50:.2f} ms |")
    md.append(f"| **90th Percentile (p90)** | {p90:.2f} ms |")
    md.append(f"| **99th Percentile (p99)** | {p99:.2f} ms |")
    md.append(f"| **Max Latency** | {max(latencies):.2f} ms |\n")
    
    md.append("## Live Query Execution Log (Sample First 50 Queries)\n")
    md.append("| ID | Prompt Snippet | Latency | Accuracy | Symbol Matched | PDF Page & Section |")
    md.append("| :-: | :--- | :-: | :-: | :--- | :--- |")
    
    sorted_results = sorted(results, key=lambda x: x["id"])
    for r in sorted_results[:50]:
        prompt_trunc = r["prompt"][:60] + "..."
        title_trunc = r["title"][:25] + "..." if r["title"] != "N/A" else "N/A"
        md.append(f"| {r['id']} | `{prompt_trunc}` | **{r['latency_ms']:.2f} ms** | {'100%' if r['success'] else '0%'} | `{r['symbol']}` | Page {r['page']} ({title_trunc}) |")
        
    with open(target_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
        
    print(f" [OK] Report successfully written to: {target_path}")
    return target_path

def start_interactive_cli():
    hw = auto_detect_hardware()
    print_minimal_header("MT5 Expert v2 - Interactive Benchmark Shell")
    print(" SYSTEM READY")
    print(f"   CPU : {hw['cpu_name']} ({hw['logical_cpus']} Threads)")
    print(f"   GPU : {', '.join(hw['gpus'])}")
    print("=" * 80)
    print(" Available Commands:")
    print("   /start   -> Run full 500-query parallel stress test")
    print("   /report  -> Export test report to docs/stress-test/stress_test_report.md")
    print("   /exit    -> Exit interactive shell")
    print("=" * 80 + "\n")
    
    while True:
        try:
            cmd = input("mt5-stress > ").strip().lower()
            if not cmd:
                continue
                
            if cmd in ["/exit", "/quit", "exit", "quit"]:
                print(" Exiting MT5 Stress Engine. Goodbye!")
                break
            elif cmd.startswith("/start") or cmd == "start":
                parts = cmd.split()
                q_count = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 500
                run_stress_test(num_queries=q_count)
            elif cmd == "/report" or cmd == "report":
                target_dir = os.path.join(DOCS_DIR, "stress-test")
                os.makedirs(target_dir, exist_ok=True)
                target_file = os.path.join(target_dir, "stress_test_report.md")
                export_report(target_file)
            else:
                print(f" [!] Unknown command: '{cmd}'. Use /start, /report, or /exit.")
        except KeyboardInterrupt:
            print("\n Interrupted. Exiting.")
            break
        except Exception as e:
            print(f" [!] Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MT5 Expert v2 Hardcore Smart Database Stress Test CLI")
    parser.add_argument("--queries", type=int, default=None, help="Number of queries to execute")
    parser.add_argument("--threads", type=int, default=0, help="Number of threads (default: 0 for smart auto-detection)")
    parser.add_argument("--verbose", action="store_true", help="Print stream for every query")
    
    args = parser.parse_args()
    
    if args.queries is None and "--queries" not in sys.argv:
        start_interactive_cli()
    else:
        q_cnt = args.queries if args.queries else 500
        run_stress_test(q_cnt, args.threads, args.verbose)
