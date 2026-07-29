# MQL5 Indicators & Technical Analysis Reference Guide

## 1. Indicator Handles & Buffer Copying
Technical indicators in MQL5 use handles (`iMA`, `iRSI`, `iBands`, `iATR`, `iCustom`). Data is extracted into arrays via `CopyBuffer`.

```mql5
int handle = iMA(_Symbol, _Period, 20, 0, MODE_EMA, PRICE_CLOSE);
double buffer[];
ArraySetAsSeries(buffer, true);

if(CopyBuffer(handle, 0, 0, 3, buffer) >= 3)
{
   double currentVal  = buffer[0];
   double previousVal = buffer[1];
}
```

---

## 2. Custom Indicator Plots & Property Declarations

```mql5
#property indicator_separate_window
#property indicator_buffers 2
#property indicator_plots   1

#property indicator_label1  "Color RSI Oscillator"
#property indicator_type1   DRAW_COLOR_LINE
#property indicator_color1  clrGreen, clrRed, clrGray
#property indicator_style1  STYLE_SOLID
#property indicator_width1  2

double ExtRsiBuffer[];
double ExtColorBuffer[];

int OnInit()
{
   SetIndexBuffer(0, ExtRsiBuffer, INDICATOR_DATA);
   SetIndexBuffer(1, ExtColorBuffer, INDICATOR_COLOR_INDEX);
   
   ArraySetAsSeries(ExtRsiBuffer, true);
   ArraySetAsSeries(ExtColorBuffer, true);
   
   return(INIT_SUCCEEDED);
}
```
