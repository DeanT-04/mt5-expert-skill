# MQL5 Trade & Position Management Reference Guide

## 1. Standard OOP Trade Classes

- `CTrade`: Market & pending order placement (`Buy`, `Sell`, `BuyLimit`, `SellLimit`, `PositionClose`, `PositionModify`).
- `CPositionInfo`: Select and inspect active position data (`Ticket`, `Symbol`, `Magic`, `PriceOpen`, `StopLoss`, `TakeProfit`).
- `CSymbolInfo`: Real-time market rates and normalization (`Ask`, `Bid`, `Point`, `Digits`, `LotsMin`, `LotsMax`, `LotsStep`).
- `CAccountInfo`: Account details (`Equity`, `Balance`, `FreeMargin`, `MarginLevel`).

---

## 2. Order Placement & Price Normalization

### Market Buy
```mql5
bool OpenBuy(double lot, double sl_points, double tp_points)
{
   m_symbol.RefreshRates();
   double ask = m_symbol.Ask();
   double sl  = (sl_points > 0) ? m_symbol.NormalizePrice(ask - sl_points * m_symbol.Point()) : 0;
   double tp  = (tp_points > 0) ? m_symbol.NormalizePrice(ask + tp_points * m_symbol.Point()) : 0;

   return m_trade.Buy(lot, _Symbol, ask, sl, tp, "Strategy Buy");
}
```

### Market Sell
```mql5
bool OpenSell(double lot, double sl_points, double tp_points)
{
   m_symbol.RefreshRates();
   double bid = m_symbol.Bid();
   double sl  = (sl_points > 0) ? m_symbol.NormalizePrice(bid + sl_points * m_symbol.Point()) : 0;
   double tp  = (tp_points > 0) ? m_symbol.NormalizePrice(bid - tp_points * m_symbol.Point()) : 0;

   return m_trade.Sell(lot, _Symbol, bid, sl, tp, "Strategy Sell");
}
```

---

## 3. Position Iteration & Filtering
Always iterate backwards from `PositionsTotal() - 1` and check `Symbol()` and `Magic()`:

```mql5
int GetPositionCount(ENUM_POSITION_TYPE type = -1)
{
   int count = 0;
   for(int i = PositionsTotal() - 1; i >= 0; i--)
   {
      ulong ticket = PositionGetTicket(i);
      if(ticket > 0 && m_position.SelectByTicket(ticket))
      {
         if(m_position.Symbol() == _Symbol && m_position.Magic() == InpMagicNumber)
         {
            if(type == -1 || m_position.PositionType() == type)
               count++;
         }
      }
   }
   return count;
}
```
