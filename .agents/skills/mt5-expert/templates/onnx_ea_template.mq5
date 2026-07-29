//+------------------------------------------------------------------+
//|                                             onnx_ea_template.mq5 |
//|                                  Copyright 2026, MetaQuotes Ltd. |
//|                                             https://www.mql5.com |
//+------------------------------------------------------------------+
#property copyright "Copyright 2026, MetaQuotes Ltd."
#property link      "https://www.mql5.com"
#property version   "1.00"
#property description "Production Machine Learning ONNX EA Template for MT5 Expert v2"

#include <Trade\Trade.mqh>
#include <Trade\SymbolInfo.mqh>

input string InpModelFilename = "model.onnx"; // Model filename in MQL5\Files
input ulong  InpMagicNumber   = 777999;       // Magic Number

CTrade      m_trade;
CSymbolInfo m_symbol;
long        m_onnxHandle = INVALID_HANDLE;

int OnInit()
{
   if(!m_symbol.Name(_Symbol)) return(INIT_FAILED);
   m_trade.SetExpertMagicNumber(InpMagicNumber);
   m_trade.SetTypeFillingBySymbol(_Symbol);

   m_onnxHandle = OnnxCreate(InpModelFilename, ONNX_DEFAULT);
   if(m_onnxHandle == INVALID_HANDLE)
   {
      PrintFormat("Failed to load ONNX model %s. Error: %d", InpModelFilename, GetLastError());
      return(INIT_FAILED);
   }

   long inputShape[] = {1, 5};
   long outputShape[] = {1, 2};

   if(!OnnxSetInputShape(m_onnxHandle, 0, inputShape) || !OnnxSetOutputShape(m_onnxHandle, 0, outputShape))
   {
      Print("Error setting ONNX tensor dimensions");
      return(INIT_FAILED);
   }

   return(INIT_SUCCEEDED);
}

void OnDeinit(const int reason)
{
   if(m_onnxHandle != INVALID_HANDLE)
   {
      OnnxRelease(m_onnxHandle);
      m_onnxHandle = INVALID_HANDLE;
   }
}

void OnTick()
{
   // Machine learning model prediction & execution loop
}
