//+------------------------------------------------------------------+
//|                                                 ea_template.mq5 |
//|                                  Copyright 2026, MetaQuotes Ltd. |
//|                                             https://www.mql5.com |
//+------------------------------------------------------------------+
#property copyright "Copyright 2026, MetaQuotes Ltd."
#property link      "https://www.mql5.com"
#property version   "1.00"
#property description "Production OOP EA Template for MT5 Expert v2"

#include <Trade\Trade.mqh>
#include <Trade\PositionInfo.mqh>
#include <Trade\SymbolInfo.mqh>
#include <Trade\AccountInfo.mqh>

input group "=== Risk & Money Management ==="
input double   InpRiskPercent       = 1.0;       // Risk % per trade
input double   InpFixedLotSize      = 0.1;       // Fixed Lot Size
input double   InpStopLossPoints    = 200.0;     // Stop Loss (Points)
input double   InpTakeProfitPoints  = 400.0;     // Take Profit (Points)
input double   InpMaxSpreadPoints   = 35.0;      // Max Allowable Spread (Points)

input group "=== Strategy Inputs ==="
input ulong    InpMagicNumber       = 888123;    // Magic Number
input int      InpMAPeriod          = 20;        // MA Period

CTrade        m_trade;
CPositionInfo m_position;
CSymbolInfo   m_symbol;
CAccountInfo  m_account;

int           m_maHandle = INVALID_HANDLE;
datetime      m_lastBar  = 0;

int OnInit()
{
   if(!m_symbol.Name(_Symbol)) return(INIT_FAILED);
   m_symbol.Refresh();

   m_trade.SetExpertMagicNumber(InpMagicNumber);
   m_trade.SetTypeFillingBySymbol(_Symbol);

   m_maHandle = iMA(_Symbol, _Period, InpMAPeriod, 0, MODE_EMA, PRICE_CLOSE);
   if(m_maHandle == INVALID_HANDLE) return(INIT_FAILED);

   return(INIT_SUCCEEDED);
}

void OnDeinit(const int reason)
{
   if(m_maHandle != INVALID_HANDLE) IndicatorRelease(m_maHandle);
}

void OnTick()
{
   // Manage existing positions
   
   // New Bar Execution Filter
   datetime currentBar = iTime(_Symbol, _Period, 0);
   if(currentBar == m_lastBar) return;
   m_lastBar = currentBar;

   // Check spread
   if(SymbolInfoInteger(_Symbol, SYMBOL_SPREAD) > (long)InpMaxSpreadPoints) return;

   // Signal evaluation logic
}
