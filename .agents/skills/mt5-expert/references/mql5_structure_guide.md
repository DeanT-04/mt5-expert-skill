# MQL5 Standard Structure & Lifecycle Reference Guide

## 1. Compiler Preprocessors & Directives
Every MQL5 Expert Advisor or Indicator begins with standard preprocessor headers:

```mql5
//+------------------------------------------------------------------+
//|                                                   MyStrategy.mq5 |
//|                                  Copyright 2026, MetaQuotes Ltd. |
//|                                             https://www.mql5.com |
//+------------------------------------------------------------------+
#property copyright "Copyright 2026, MetaQuotes Ltd."
#property link      "https://www.mql5.com"
#property version   "1.00"
#property description "Production-Grade OOP EA Architecture"
```

---

## 2. Standard Header Includes
Include Standard Library headers for trading, positions, symbols, and indicators:

```mql5
#include <Trade\Trade.mqh>
#include <Trade\PositionInfo.mqh>
#include <Trade\SymbolInfo.mqh>
#include <Trade\AccountInfo.mqh>
```

---

## 3. Input Directives & Parameter Groups
Organize user inputs into clean GUI sections using `group`:

```mql5
input group "=== Money Management ==="
input double InpRiskPercent     = 1.0;       // Account Risk % per Trade
input double InpFixedLot        = 0.1;       // Fixed Lot Size (if Risk % == 0)
input double InpStopLossPoints  = 200.0;     // Stop Loss (Points)
input double InpTakeProfitPoints= 400.0;     // Take Profit (Points)

input group "=== Strategy Parameters ==="
input ulong  InpMagicNumber     = 999123;    // Magic Number
input int    InpPeriod          = 14;        // Indicator Period
```

---

## 4. Primary Lifecycle Handlers

### `OnInit()`
Triggered when EA/Indicator loads on a chart. Must return `INIT_SUCCEEDED`, `INIT_FAILED`, or `INIT_PARAMETERS_INCORRECT`.

```mql5
int OnInit()
{
   if(!m_symbol.Name(_Symbol)) return(INIT_FAILED);
   m_symbol.Refresh();

   m_trade.SetExpertMagicNumber(InpMagicNumber);
   m_trade.SetTypeFillingBySymbol(_Symbol);

   return(INIT_SUCCEEDED);
}
```

### `OnDeinit(const int reason)`
Triggered when EA is removed, timeframe changed, or terminal closed.

```mql5
void OnDeinit(const int reason)
{
   if(handle != INVALID_HANDLE)
      IndicatorRelease(handle);
}
```

### `OnTick()`
Executed on every incoming tick for Expert Advisors.

```mql5
void OnTick()
{
   // Manage positions and check signals
}
```
