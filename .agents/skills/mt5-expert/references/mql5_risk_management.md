# MQL5 Risk & Money Management Reference Guide

## 1. Dynamic Lot Sizing (% Equity / Margin Risk)

```mql5
double CalculateLotSize(double sl_points, double risk_percent)
{
   if(sl_points <= 0 || risk_percent <= 0) return InpFixedLot;

   double equity     = m_account.Equity();
   double riskAmount = equity * (risk_percent / 100.0);

   double tickValue  = m_symbol.TickValue();
   double tickSize   = m_symbol.TickSize();
   double point      = m_symbol.Point();

   if(tickValue <= 0 || tickSize <= 0 || point <= 0) return InpFixedLot;

   double pointValue = (tickValue / tickSize) * point;
   double rawLot     = riskAmount / (sl_points * pointValue);

   double minLot  = m_symbol.LotsMin();
   double maxLot  = m_symbol.LotsMax();
   double lotStep = m_symbol.LotsStep();

   double lot = MathFloor(rawLot / lotStep) * lotStep;
   if(lot < minLot) lot = minLot;
   if(lot > maxLot) lot = maxLot;

   return lot;
}
```

---

## 2. Dynamic Trailing Stop Loss & Break-Even

```mql5
void ManageTrailingAndBreakEven(double trail_points, double be_trigger, double be_lock)
{
   m_symbol.RefreshRates();
   double point = m_symbol.Point();

   for(int i = PositionsTotal() - 1; i >= 0; i--)
   {
      ulong ticket = PositionGetTicket(i);
      if(ticket > 0 && m_position.SelectByTicket(ticket))
      {
         if(m_position.Symbol() == _Symbol && m_position.Magic() == InpMagicNumber)
         {
            double openPrice = m_position.PriceOpen();
            double currentSl = m_position.StopLoss();

            if(m_position.PositionType() == POSITION_TYPE_BUY)
            {
               double bid = m_symbol.Bid();
               // Break-even
               if(be_trigger > 0 && (bid - openPrice >= be_trigger * point))
               {
                  double beSl = m_symbol.NormalizePrice(openPrice + be_lock * point);
                  if(currentSl < beSl)
                     m_trade.PositionModify(ticket, beSl, m_position.TakeProfit());
               }
               // Trailing Stop
               if(trail_points > 0 && (bid - openPrice > trail_points * point))
               {
                  double newSl = m_symbol.NormalizePrice(bid - trail_points * point);
                  if(newSl > currentSl)
                     m_trade.PositionModify(ticket, newSl, m_position.TakeProfit());
               }
            }
         }
      }
   }
}
```
