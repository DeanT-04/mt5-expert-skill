# MQL5 MetaEditor Compilation Errors & Repair Patterns

## 1. Common MetaEditor Errors & Resolutions

| Error Code | Error Message | Cause & Fix Strategy |
| :--- | :--- | :--- |
| **error 123** | `'X' - undeclared identifier` | Symbol `X` is used without declaration. Add `#include <Trade\Trade.mqh>` or declare `X`. |
| **error 140** | `parameter conversion not allowed` | Mismatch in parameter types. Cast variable explicitly `(ulong)var` or `(int)var`. |
| **error 120** | `not all control paths return a value` | Non-void function (`int OnInit()`) missing `return` statement in a branch. Add `return INIT_SUCCEEDED;`. |
| **error 148** | `array out of range` | Accessing element outside array bounds. Check `ArraySize(arr)` or `rates_total`. |
| **error 156** | `'trade' - struct / class undefined` | Using `CTrade` without `#include <Trade\Trade.mqh>`. Add include. |

---

## 2. MetaEditor Warnings & Clean Code Fixes

- **Implicit conversion warning**:
  `Print("Val: " + val);` -> Use `PrintFormat("Val: %.2f", val);`
- **Unreferenced formal parameter warning**:
  `void OnDeinit(const int reason)` -> Add `(void)reason;` to clear warning.
