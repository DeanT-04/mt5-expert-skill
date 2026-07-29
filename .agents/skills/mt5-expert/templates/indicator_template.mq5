//+------------------------------------------------------------------+
//|                                          indicator_template.mq5 |
//|                                  Copyright 2026, MetaQuotes Ltd. |
//|                                             https://www.mql5.com |
//+------------------------------------------------------------------+
#property copyright "Copyright 2026, MetaQuotes Ltd."
#property link      "https://www.mql5.com"
#property version   "1.00"
#property description "Production Custom Indicator Template for MT5 Expert v2"

#property indicator_separate_window
#property indicator_buffers 2
#property indicator_plots   1

#property indicator_label1  "Custom Signal Buffer"
#property indicator_type1   DRAW_COLOR_LINE
#property indicator_color1  clrGreen, clrRed, clrGray
#property indicator_style1  STYLE_SOLID
#property indicator_width1  2

input int InpPeriod = 14;

double ExtBuffer[];
double ExtColorBuffer[];

int OnInit()
{
   SetIndexBuffer(0, ExtBuffer, INDICATOR_DATA);
   SetIndexBuffer(1, ExtColorBuffer, INDICATOR_COLOR_INDEX);

   ArraySetAsSeries(ExtBuffer, true);
   ArraySetAsSeries(ExtColorBuffer, true);

   return(INIT_SUCCEEDED);
}

int OnCalculate(const int rates_total,
                const int prev_calculated,
                const datetime &time[],
                const double &open[],
                const double &high[],
                const double &low[],
                const double &close[],
                const long &tick_volume[],
                const long &volume[],
                const int &spread[])
{
   if(rates_total < InpPeriod) return(0);

   int limit = rates_total - prev_calculated;
   if(prev_calculated > 0) limit++;

   for(int i = limit - 1; i >= 0; i--)
   {
      ExtBuffer[i] = close[i];
      ExtColorBuffer[i] = (close[i] > open[i]) ? 0.0 : 1.0;
   }

   return(rates_total);
}
