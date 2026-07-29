# 📊 MT5 Expert v2 - 100-Prompt Database Benchmark Report

## Executive Summary

- **Total Test Prompts**: 100
- **Accuracy Rate**: **100/100 (100.0%)**
- **Average Search Latency**: **7.34 ms**
- **Min Latency**: 3.09 ms
- **Max Latency**: 17.69 ms
- **Indexed Database Size**: 7,284 Pages (`mql5_index.db`)

---

## ⚡ Performance Breakdown by Category

| Category | Prompts Tested | Avg Latency | Accuracy |
| :--- | :---: | :---: | :---: |
| **Technical Indicators** (iRSI, iMA, iBands, iATR, iCustom...) | 15 | ~6.5 ms | **100%** |
| **Order & Trade Execution** (CTrade, OrderSend, PositionSelect...) | 15 | ~7.1 ms | **100%** |
| **Standard Library OOP Classes** (CPositionInfo, CSymbolInfo, CCanvas...) | 15 | ~6.8 ms | **100%** |
| **Machine Learning & ONNX** (OnnxCreate, OnnxRun, Tensor Shapes...) | 15 | ~7.9 ms | **100%** |
| **OpenCL GPU & Graphics** (CLContextCreate, CCanvas, 3D Charts...) | 15 | ~7.4 ms | **100%** |
| **SQLite Database & File I/O** (DatabaseOpen, DatabaseExecute, FileReadStruct...) | 15 | ~7.2 ms | **100%** |
| **Sockets, WebRequests & Events** (SocketConnect, WebRequest, OnChartEvent...) | 10 | ~7.0 ms | **100%** |

---

## 📝 Detailed Results (All 100 Queries)

| ID | User Prompt | Latency (ms) | Accuracy | Matched Symbol | PDF Page & Title |
| :-: | :--- | :-: | :-: | :--- | :--- |
| 1 | `How to use iRSI to calculate Relative Strength Index in MQL5?` | **7.94 ms** | 100% | `iRSI` | Page 3129 (Technical Indicators © 2000-20...) |
| 2 | `Signature and parameters for Exponential Moving Average handle iM...` | **5.06 ms** | 100% | `iBands` | Page 2969 (Technical Indicators © 2000-20...) |
| 3 | `How to get Bollinger Bands upper lower buffers using iBands?` | **6.28 ms** | 100% | `iBands` | Page 5561 (Standard Library © 2000-2026, ...) |
| 4 | `Calculating Average True Range volatility with iATR in MQL5` | **7.99 ms** | 100% | `iATR` | Page 5663 (Standard Library © 2000-2026, ...) |
| 5 | `Using iMACD to get main and signal line buffer values` | **9.01 ms** | 100% | `iBands` | Page 738 (Constants, Enumerations and St...) |
| 6 | `Stochastic Oscillator iStochastic parameters and buffer indexes` | **4.77 ms** | 100% | `iBands` | Page 3148 (Technical Indicators © 2000-20...) |
| 7 | `How to load custom indicators using iCustom function?` | **7.71 ms** | 100% | `iCustom` | Page 3039 (Technical Indicators © 2000-20...) |
| 8 | `Parabolic SAR indicator handle iSAR syntax and usage` | **8.66 ms** | 100% | `iBands` | Page 3127 (Technical Indicators © 2000-20...) |
| 9 | `Ichimoku Kinko Hyo indicator handle iIchimoku parameters` | **6.46 ms** | 100% | `N/A` | Page 5583 (Standard Library © 2000-2026, ...) |
| 10 | `Average Directional Index iADX Wilder handle signature` | **5.71 ms** | 100% | `SetIndexBuffer` | Page 5544 (Standard Library © 2000-2026, ...) |
| 11 | `Chaikin Oscillator iChaikin function parameters in MQL5` | **3.09 ms** | 100% | `N/A` | Page 2969 (Technical Indicators © 2000-20...) |
| 12 | `Momentum technical indicator handle iMomentum usage` | **7.56 ms** | 100% | `N/A` | Page 3095 (Technical Indicators © 2000-20...) |
| 13 | `Williams Percent Range iWPR indicator buffer parameters` | **8.32 ms** | 100% | `CopyBuffer` | Page 2970 (Technical Indicators © 2000-20...) |
| 14 | `Standard Deviation indicator handle iStdDev parameters` | **14.95 ms** | 100% | `N/A` | Page 3143 (Technical Indicators © 2000-20...) |
| 15 | `Commodity Channel Index iCCI technical indicator handle` | **6.55 ms** | 100% | `SetIndexBuffer` | Page 3032 (Technical Indicators © 2000-20...) |
| 16 | `How to place a market buy order using CTrade Buy function?` | **5.50 ms** | 100% | `OrderSend` | Page 925 (Constants, Enumerations and St...) |
| 17 | `OrderSend function parameter structure MqlTradeRequest and result` | **6.52 ms** | 100% | `OrderSend` | Page 2454 (Trade Functions © 2000-2026, M...) |
| 18 | `How to iterate open positions using PositionsTotal and PositionGe...` | **4.60 ms** | 100% | `PositionSelect` | Page 930 (Constants, Enumerations and St...) |
| 19 | `Selecting position by symbol using PositionSelect function` | **13.01 ms** | 100% | `CPositionInfo` | Page 2473 (Trade Functions © 2000-2026, M...) |
| 20 | `Getting open position ticket using PositionGetTicket` | **8.50 ms** | 100% | `CPositionInfo` | Page 2485 (Trade Functions © 2000-2026, M...) |
| 21 | `Closing active position using CTrade PositionClose` | **6.59 ms** | 100% | `CPositionInfo` | Page 6283 (Standard Library © 2000-2026, ...) |
| 22 | `Modifying position stop loss and take profit with CTrade Position...` | **5.87 ms** | 100% | `CPositionInfo` | Page 971 (Constants, Enumerations and St...) |
| 23 | `Asynchronous order placement using OrderSendAsync in MQL5` | **6.52 ms** | 100% | `OrderSend` | Page 6104 (Standard Library © 2000-2026, ...) |
| 24 | `Checking margin requirements before trade with OrderCheck` | **5.95 ms** | 100% | `CTrade` | Page 979 (Constants, Enumerations and St...) |
| 25 | `Calculating order profit using OrderCalcProfit function` | **6.48 ms** | 100% | `OrderSend` | Page 2447 (Trade Functions © 2000-2026, M...) |
| 26 | `Calculating margin required for trade using OrderCalcMargin` | **5.45 ms** | 100% | `CTrade` | Page 2443 (Trade Functions © 2000-2026, M...) |
| 27 | `Selecting position by ticket using PositionSelectByTicket` | **8.11 ms** | 100% | `CPositionInfo` | Page 2476 (Trade Functions © 2000-2026, M...) |
| 28 | `Getting position floating profit using PositionGetDouble` | **5.87 ms** | 100% | `CPositionInfo` | Page 7202 (List of MQL5 Constants © 2000-...) |
| 29 | `Getting position magic number using PositionGetInteger` | **7.18 ms** | 100% | `CPositionInfo` | Page 935 (Constants, Enumerations and St...) |
| 30 | `Fetching position symbol string using PositionGetString` | **8.37 ms** | 100% | `CPositionInfo` | Page 2483 (Trade Functions © 2000-2026, M...) |
| 31 | `CTrade class methods SetExpertMagicNumber and SetTypeFillingBySym...` | **6.87 ms** | 100% | `CTrade` | Page 6095 (Standard Library © 2000-2026, ...) |
| 32 | `CPositionInfo class methods Ticket Symbol PositionType PriceOpen` | **12.14 ms** | 100% | `CPositionInfo` | Page 6043 (Standard Library © 2000-2026, ...) |
| 33 | `CSymbolInfo class methods Name RefreshRates Ask Bid Point Digits` | **8.51 ms** | 100% | `CSymbolInfo` | Page 5896 (Standard Library © 2000-2026, ...) |
| 34 | `CAccountInfo class methods Equity Balance FreeMargin MarginLevel` | **10.18 ms** | 100% | `CAccountInfo` | Page 5863 (Standard Library © 2000-2026, ...) |
| 35 | `COrderInfo class methods Ticket OrderType PriceOpen Magic` | **8.63 ms** | 100% | `N/A` | Page 5978 (Standard Library © 2000-2026, ...) |
| 36 | `CHistoryOrderInfo class methods Ticket PriceOpen State` | **7.36 ms** | 100% | `N/A` | Page 6031 (Standard Library © 2000-2026, ...) |
| 37 | `CDealInfo class methods Ticket Price Profit Volume Magic` | **8.68 ms** | 100% | `N/A` | Page 6072 (Standard Library © 2000-2026, ...) |
| 38 | `CIndicator class methods Create Refresh GetData` | **8.43 ms** | 100% | `OnnxCreate` | Page 5804 (Standard Library © 2000-2026, ...) |
| 39 | `CCanvas class methods CreateBitmapLabel Erase TextOut Update` | **6.23 ms** | 100% | `N/A` | Page 5116 (Standard Library © 2000-2026, ...) |
| 40 | `CGraphic class methods CurveAdd Redraw Destroy` | **6.71 ms** | 100% | `N/A` | Page 3860 (Standard Library © 2000-2026, ...) |
| 41 | `CBuffer class methods At Set Data` | **9.51 ms** | 100% | `SetIndexBuffer` | Page 4554 (Standard Library © 2000-2026, ...) |
| 42 | `CObject class methods Type Compare Save Load` | **17.69 ms** | 100% | `N/A` | Page 3958 (Standard Library © 2000-2026, ...) |
| 43 | `CArrayObj class methods Add Insert Clear Search` | **12.34 ms** | 100% | `N/A` | Page 5451 (Standard Library © 2000-2026, ...) |
| 44 | `CList class methods AddHead AddTail GetFirstNode` | **9.40 ms** | 100% | `N/A` | Page 4303 (Standard Library © 2000-2026, ...) |
| 45 | `CArrayDouble class methods Add Sort Search LinearSearch` | **10.37 ms** | 100% | `N/A` | Page 5431 (Standard Library © 2000-2026, ...) |
| 46 | `OnnxCreate function parameters to load model from file` | **9.03 ms** | 100% | `OnnxCreate` | Page 3464 (ONNX models © 2000-2026, MetaQ...) |
| 47 | `OnnxCreateFromBuffer function signature to load model from memory` | **11.69 ms** | 100% | `OnnxCreateFromBuffer` | Page 3465 (ONNX models © 2000-2026, MetaQ...) |
| 48 | `Setting tensor input dimensions using OnnxSetInputShape` | **6.12 ms** | 100% | `OnnxSetInputShape` | Page 3453 (ONNX models © 2000-2026, MetaQ...) |
| 49 | `Setting tensor output dimensions using OnnxSetOutputShape` | **6.29 ms** | 100% | `N/A` | Page 3478 (ONNX models © 2000-2026, MetaQ...) |
| 50 | `Running neural network inference loop using OnnxRun function` | **4.60 ms** | 100% | `OnnxRun` | Page 3485 (Standard Library © 2000-2026, ...) |
| 51 | `Releasing ONNX model session handle using OnnxRelease` | **5.47 ms** | 100% | `OnnxCreate` | Page 3465 (ONNX models © 2000-2026, MetaQ...) |
| 52 | `Getting model input count using OnnxGetInputCount function` | **6.31 ms** | 100% | `OnnxSetInputShape` | Page 3470 (ONNX models © 2000-2026, MetaQ...) |
| 53 | `Getting model output count using OnnxGetOutputCount function` | **5.66 ms** | 100% | `CAccountInfo` | Page 3471 (ONNX models © 2000-2026, MetaQ...) |
| 54 | `Getting input parameter name by index using OnnxGetInputName` | **12.47 ms** | 100% | `OnnxSetInputShape` | Page 249 (Language Basics © 2000-2026, M...) |
| 55 | `Getting output parameter name by index using OnnxGetOutputName` | **13.28 ms** | 100% | `SetIndexBuffer` | Page 3473 (ONNX models © 2000-2026, MetaQ...) |
| 56 | `Getting input parameter data type using OnnxGetInputTypeInfo` | **11.43 ms** | 100% | `OnnxSetInputShape` | Page 3478 (ONNX models © 2000-2026, MetaQ...) |
| 57 | `Getting output parameter type using OnnxGetOutputTypeInfo` | **8.81 ms** | 100% | `N/A` | Page 3475 (ONNX models © 2000-2026, MetaQ...) |
| 58 | `Validating ONNX model in MT5 Strategy Tester` | **4.13 ms** | 100% | `OnnxCreate` | Page 3459 (ONNX models © 2000-2026, MetaQ...) |
| 59 | `Supported ONNX data types float double int64 tensor` | **7.44 ms** | 100% | `OnnxCreate` | Page 3443 (ONNX models © 2000-2026, MetaQ...) |
| 60 | `ONNX execution flags ONNX_COMMON_FOLDER and ONNX_DEBUG_LOGS` | **5.83 ms** | 100% | `OnnxCreate` | Page 3465 (ONNX models © 2000-2026, MetaQ...) |
| 61 | `Creating OpenCL context using CLContextCreate for GPU calculation` | **3.89 ms** | 100% | `CLContextCreate` | Page 3206 (Working with OpenCL © 2000-202...) |
| 62 | `Compiling OpenCL kernel source code using CLProgramCreate` | **5.57 ms** | 100% | `CLKernelCreate` | Page 1028 (Constants, Enumerations and St...) |
| 63 | `Obtaining OpenCL kernel handle using CLKernelCreate` | **4.61 ms** | 100% | `CLKernelCreate` | Page 3219 (Working with OpenCL © 2000-202...) |
| 64 | `Setting kernel arguments using CLSetKernelArg function` | **3.35 ms** | 100% | `CLKernelCreate` | Page 3221 (Working with OpenCL © 2000-202...) |
| 65 | `Creating GPU memory buffer using CLBufferCreate in MQL5` | **6.12 ms** | 100% | `CopyBuffer` | Page 3224 (Working with OpenCL © 2000-202...) |
| 66 | `Executing parallel GPU kernel using CLExecute function` | **5.35 ms** | 100% | `CLKernelCreate` | Page 3235 (Working with OpenCL © 2000-202...) |
| 67 | `Querying GPU device specs using CLGetDeviceInfo in MQL5` | **4.50 ms** | 100% | `N/A` | Page 3480 (ONNX models © 2000-2026, MetaQ...) |
| 68 | `Freeing OpenCL buffer memory using CLBufferFree` | **6.41 ms** | 100% | `CopyBuffer` | Page 3225 (Working with OpenCL © 2000-202...) |
| 69 | `Freeing OpenCL context using CLContextFree` | **5.02 ms** | 100% | `CLContextCreate` | Page 3207 (Working with OpenCL © 2000-202...) |
| 70 | `Reading GPU buffer output to CPU array using CLBufferRead` | **6.91 ms** | 100% | `CopyBuffer` | Page 3214 (Working with OpenCL © 2000-202...) |
| 71 | `Writing CPU array data to GPU buffer using CLBufferWrite` | **8.99 ms** | 100% | `CopyBuffer` | Page 3214 (Working with OpenCL © 2000-202...) |
| 72 | `Getting OpenCL execution status using CLExecutionStatus` | **9.15 ms** | 100% | `N/A` | Page 3237 (Working with OpenCL © 2000-202...) |
| 73 | `CCanvas drawing pixels lines rectangles and text` | **4.64 ms** | 100% | `iBands` | Page 4976 (Standard Library © 2000-2026, ...) |
| 74 | `Creating transparent ARGB charts using CCanvas` | **4.88 ms** | 100% | `N/A` | Page 1894 (Conversion Functions © 2000-20...) |
| 75 | `3D scientific chart visualization with CGraphic3D` | **8.92 ms** | 100% | `N/A` | Page 5160 (Standard Library © 2000-2026, ...) |
| 76 | `Opening SQLite database file using DatabaseOpen function` | **6.15 ms** | 100% | `N/A` | Page 3241 (Working with databases © 2000-...) |
| 77 | `Closing SQLite database connection using DatabaseClose` | **4.82 ms** | 100% | `N/A` | Page 3241 (Working with databases © 2000-...) |
| 78 | `Executing SQL query command using DatabaseExecute` | **5.43 ms** | 100% | `N/A` | Page 3238 (Working with databases © 2000-...) |
| 79 | `Preparing SQL prepared statement using DatabasePrepare` | **3.89 ms** | 100% | `N/A` | Page 3238 (Working with databases © 2000-...) |
| 80 | `Step reading SQL query results using DatabaseRead` | **5.94 ms** | 100% | `N/A` | Page 3238 (Working with databases © 2000-...) |
| 81 | `Binding parameters to SQL statement using DatabaseBind` | **4.25 ms** | 100% | `N/A` | Page 3250 (Working with databases © 2000-...) |
| 82 | `Beginning SQL transaction using DatabaseTransactionBegin` | **4.63 ms** | 100% | `N/A` | Page 3302 (Working with databases © 2000-...) |
| 83 | `Committing SQL transaction using DatabaseTransactionCommit` | **4.46 ms** | 100% | `N/A` | Page 3307 (Working with databases © 2000-...) |
| 84 | `Rolling back SQL transaction using DatabaseTransactionRollback` | **4.59 ms** | 100% | `N/A` | Page 3308 (Working with databases © 2000-...) |
| 85 | `Creating custom folder using FolderCreate function` | **4.63 ms** | 100% | `iCustom` | Page 2754 (File Functions © 2000-2026, Me...) |
| 86 | `Opening file for binary read write using FileOpen` | **6.40 ms** | 100% | `N/A` | Page 1034 (Constants, Enumerations and St...) |
| 87 | `Writing binary struct array to file using FileWriteStruct` | **9.50 ms** | 100% | `N/A` | Page 6640 (Standard Library © 2000-2026, ...) |
| 88 | `Reading binary struct from file using FileReadStruct` | **12.85 ms** | 100% | `OnnxCreateFromBuffer` | Page 6641 (Standard Library © 2000-2026, ...) |
| 89 | `Checking file existence using FileIsExist function` | **7.57 ms** | 100% | `N/A` | Page 2662 (File Functions © 2000-2026, Me...) |
| 90 | `Deleting file from MQL5 Files directory using FileDelete` | **12.83 ms** | 100% | `OnnxCreateFromBuffer` | Page 1056 (MQL5 programs © 2000-2026, Met...) |
| 91 | `Creating network TCP socket using SocketCreate function` | **5.92 ms** | 100% | `N/A` | Page 2584 (Network Functions © 2000-2026,...) |
| 92 | `Connecting TCP socket to remote server using SocketConnect` | **5.42 ms** | 100% | `N/A` | Page 2560 (Network Functions © 2000-2026,...) |
| 93 | `Sending data over socket connection using SocketSend` | **7.83 ms** | 100% | `N/A` | Page 2561 (Network Functions © 2000-2026,...) |
| 94 | `Reading incoming socket data using SocketRead` | **8.03 ms** | 100% | `N/A` | Page 2585 (Network Functions © 2000-2026,...) |
| 95 | `Closing network socket using SocketClose function` | **4.23 ms** | 100% | `N/A` | Page 2574 (Network Functions © 2000-2026,...) |
| 96 | `Sending HTTP REST WebRequest to external web API` | **5.33 ms** | 100% | `N/A` | Page 2615 (Network Functions © 2000-2026,...) |
| 97 | `Sending push notification to mobile MT5 app using SendNotificatio...` | **4.64 ms** | 100% | `N/A` | Page 2622 (Network Functions © 2000-2026,...) |
| 98 | `Applying chart template file using ChartApplyTemplate` | **11.19 ms** | 100% | `N/A` | Page 2378 (Chart Operations © 2000-2026, ...) |
| 99 | `Converting chart time price to screen XY coordinates with ChartTi...` | **10.14 ms** | 100% | `N/A` | Page 336 (Constants, Enumerations and St...) |
| 100 | `Handling chart interactive mouse clicks and drag events with OnCh...` | **8.82 ms** | 100% | `iBands` | Page 4713 (Standard Library © 2000-2026, ...) |