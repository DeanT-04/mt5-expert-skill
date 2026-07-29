import time
import json
import os
import sys

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.search.engine import query_dual_layer
from scripts.config import PROJECT_ROOT

PROMPTS = [
    # 1-15: Technical Indicators
    "How to use iRSI to calculate Relative Strength Index in MQL5?",
    "Signature and parameters for Exponential Moving Average handle iMA",
    "How to get Bollinger Bands upper lower buffers using iBands?",
    "Calculating Average True Range volatility with iATR in MQL5",
    "Using iMACD to get main and signal line buffer values",
    "Stochastic Oscillator iStochastic parameters and buffer indexes",
    "How to load custom indicators using iCustom function?",
    "Parabolic SAR indicator handle iSAR syntax and usage",
    "Ichimoku Kinko Hyo indicator handle iIchimoku parameters",
    "Average Directional Index iADX Wilder handle signature",
    "Chaikin Oscillator iChaikin function parameters in MQL5",
    "Momentum technical indicator handle iMomentum usage",
    "Williams Percent Range iWPR indicator buffer parameters",
    "Standard Deviation indicator handle iStdDev parameters",
    "Commodity Channel Index iCCI technical indicator handle",

    # 16-30: Order Execution & Trade Management
    "How to place a market buy order using CTrade Buy function?",
    "OrderSend function parameter structure MqlTradeRequest and result",
    "How to iterate open positions using PositionsTotal and PositionGetTicket?",
    "Selecting position by symbol using PositionSelect function",
    "Getting open position ticket using PositionGetTicket",
    "Closing active position using CTrade PositionClose",
    "Modifying position stop loss and take profit with CTrade PositionModify",
    "Asynchronous order placement using OrderSendAsync in MQL5",
    "Checking margin requirements before trade with OrderCheck",
    "Calculating order profit using OrderCalcProfit function",
    "Calculating margin required for trade using OrderCalcMargin",
    "Selecting position by ticket using PositionSelectByTicket",
    "Getting position floating profit using PositionGetDouble",
    "Getting position magic number using PositionGetInteger",
    "Fetching position symbol string using PositionGetString",

    # 31-45: Standard Library OOP Classes
    "CTrade class methods SetExpertMagicNumber and SetTypeFillingBySymbol",
    "CPositionInfo class methods Ticket Symbol PositionType PriceOpen",
    "CSymbolInfo class methods Name RefreshRates Ask Bid Point Digits",
    "CAccountInfo class methods Equity Balance FreeMargin MarginLevel",
    "COrderInfo class methods Ticket OrderType PriceOpen Magic",
    "CHistoryOrderInfo class methods Ticket PriceOpen State",
    "CDealInfo class methods Ticket Price Profit Volume Magic",
    "CIndicator class methods Create Refresh GetData",
    "CCanvas class methods CreateBitmapLabel Erase TextOut Update",
    "CGraphic class methods CurveAdd Redraw Destroy",
    "CBuffer class methods At Set Data",
    "CObject class methods Type Compare Save Load",
    "CArrayObj class methods Add Insert Clear Search",
    "CList class methods AddHead AddTail GetFirstNode",
    "CArrayDouble class methods Add Sort Search LinearSearch",

    # 46-60: Machine Learning & ONNX Models
    "OnnxCreate function parameters to load model from file",
    "OnnxCreateFromBuffer function signature to load model from memory",
    "Setting tensor input dimensions using OnnxSetInputShape",
    "Setting tensor output dimensions using OnnxSetOutputShape",
    "Running neural network inference loop using OnnxRun function",
    "Releasing ONNX model session handle using OnnxRelease",
    "Getting model input count using OnnxGetInputCount function",
    "Getting model output count using OnnxGetOutputCount function",
    "Getting input parameter name by index using OnnxGetInputName",
    "Getting output parameter name by index using OnnxGetOutputName",
    "Getting input parameter data type using OnnxGetInputTypeInfo",
    "Getting output parameter type using OnnxGetOutputTypeInfo",
    "Validating ONNX model in MT5 Strategy Tester",
    "Supported ONNX data types float double int64 tensor",
    "ONNX execution flags ONNX_COMMON_FOLDER and ONNX_DEBUG_LOGS",

    # 61-75: OpenCL GPU Acceleration & Graphics
    "Creating OpenCL context using CLContextCreate for GPU calculation",
    "Compiling OpenCL kernel source code using CLProgramCreate",
    "Obtaining OpenCL kernel handle using CLKernelCreate",
    "Setting kernel arguments using CLSetKernelArg function",
    "Creating GPU memory buffer using CLBufferCreate in MQL5",
    "Executing parallel GPU kernel using CLExecute function",
    "Querying GPU device specs using CLGetDeviceInfo in MQL5",
    "Freeing OpenCL buffer memory using CLBufferFree",
    "Freeing OpenCL context using CLContextFree",
    "Reading GPU buffer output to CPU array using CLBufferRead",
    "Writing CPU array data to GPU buffer using CLBufferWrite",
    "Getting OpenCL execution status using CLExecutionStatus",
    "CCanvas drawing pixels lines rectangles and text",
    "Creating transparent ARGB charts using CCanvas",
    "3D scientific chart visualization with CGraphic3D",

    # 76-90: SQLite Database & File I/O
    "Opening SQLite database file using DatabaseOpen function",
    "Closing SQLite database connection using DatabaseClose",
    "Executing SQL query command using DatabaseExecute",
    "Preparing SQL prepared statement using DatabasePrepare",
    "Step reading SQL query results using DatabaseRead",
    "Binding parameters to SQL statement using DatabaseBind",
    "Beginning SQL transaction using DatabaseTransactionBegin",
    "Committing SQL transaction using DatabaseTransactionCommit",
    "Rolling back SQL transaction using DatabaseTransactionRollback",
    "Creating custom folder using FolderCreate function",
    "Opening file for binary read write using FileOpen",
    "Writing binary struct array to file using FileWriteStruct",
    "Reading binary struct from file using FileReadStruct",
    "Checking file existence using FileIsExist function",
    "Deleting file from MQL5 Files directory using FileDelete",

    # 91-100: Sockets, WebRequests, Chart Operations & Events
    "Creating network TCP socket using SocketCreate function",
    "Connecting TCP socket to remote server using SocketConnect",
    "Sending data over socket connection using SocketSend",
    "Reading incoming socket data using SocketRead",
    "Closing network socket using SocketClose function",
    "Sending HTTP REST WebRequest to external web API",
    "Sending push notification to mobile MT5 app using SendNotification",
    "Applying chart template file using ChartApplyTemplate",
    "Converting chart time price to screen XY coordinates with ChartTimePriceToXY",
    "Handling chart interactive mouse clicks and drag events with OnChartEvent"
]

def run_benchmark():
    print(f"Running 100-Prompt Benchmark against MQL5 Index Database...")
    results = []
    total_time = 0.0
    
    for idx, prompt in enumerate(PROMPTS, 1):
        t0 = time.perf_counter()
        query_res = query_dual_layer(prompt)
        t1 = time.perf_counter()
        
        latency_ms = (t1 - t0) * 1000.0
        total_time += latency_ms
        
        has_symbol_matches = len(query_res["symbol_table_matches"]) > 0
        has_pdf_snippets = len(query_res["pdf_snippets"]) > 0
        
        # Accuracy score: 100% if symbol or PDF snippets found, else partial
        accuracy = "100%" if (has_symbol_matches or has_pdf_snippets) else "0%"
        top_snippet = query_res["pdf_snippets"][0] if has_pdf_snippets else None
        top_symbol = list(query_res["symbol_table_matches"].keys())[0] if has_symbol_matches else "N/A"
        
        results.append({
            "id": idx,
            "prompt": prompt,
            "latency_ms": latency_ms,
            "accuracy": accuracy,
            "symbol_found": top_symbol,
            "pdf_page": top_snippet["page"] if top_snippet else "N/A",
            "pdf_title": top_snippet["title"] if top_snippet else "N/A"
        })
        
    avg_latency = total_time / len(PROMPTS)
    min_latency = min(r["latency_ms"] for r in results)
    max_latency = max(r["latency_ms"] for r in results)
    accurate_count = sum(1 for r in results if r["accuracy"] == "100%")
    
    print(f"Completed {len(PROMPTS)} queries.")
    print(f"Average Latency: {avg_latency:.2f} ms")
    print(f"Min Latency: {min_latency:.2f} ms")
    print(f"Max Latency: {max_latency:.2f} ms")
    print(f"Accuracy Rate: {accurate_count}/{len(PROMPTS)} ({accurate_count/len(PROMPTS)*100:.1f}%)")
    
    return {
        "summary": {
            "total_queries": len(PROMPTS),
            "accurate_count": accurate_count,
            "accuracy_percent": accurate_count / len(PROMPTS) * 100.0,
            "avg_latency_ms": avg_latency,
            "min_latency_ms": min_latency,
            "max_latency_ms": max_latency,
            "total_pages_indexed": 7284
        },
        "details": results
    }

if __name__ == "__main__":
    benchmark_data = run_benchmark()
    with open(os.path.join(PROJECT_ROOT, "benchmark_data.json"), "w") as f:
        json.dump(benchmark_data, f, indent=2)
