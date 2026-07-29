---
name: mt5-expert
description: MetaTrader 5 (MT5) MQL5 Expert Advisor & Custom Indicator developer (Version 2 with Solution 3 Dual-Layer SQLite & Symbol Map). Activates ONLY when the user prompt STARTS with `@mt5-S` (for Strategy/EA) or `@mt5-I` (for Custom Indicator). Do NOT activate if `@mt5-S` or `@mt5-I` appears in the middle or end of the text. Encompasses the full MQL5 documentation reference, automated file deployment to MT5 Terminal directories, and headless MetaEditor64 compilation & error verification.
---

# MT5 Expert & Indicator Skill v2

Project-scoped MT5 development skill using Solution 3 (Dual-Layer SQLite FTS5 + Symbol Map) and `uv` virtual environment execution.

---

## 1. Invocation Rules & Trigger Prefix
This skill MUST be invoked ONLY when the user prompt **STARTS WITH**:
- **`@mt5-S`**: Strategy / Expert Advisor (EA) generation.
- **`@mt5-I`**: Custom Technical Indicator generation.

> [!IMPORTANT]
> If `@mt5-S` or `@mt5-I` appears anywhere else (middle or end of prompt), do NOT activate this skill.

---

## 2. Single-Source Skill Architecture & Resources

```text
.agents/skills/mt5-expert/
├── SKILL.md                          <- Main Skill instructions & frontmatter
├── references/                       <- Bundled MQL5 Reference Guides (Single Source of Truth)
│   ├── mql5_structure_guide.md       <- Headers, preprocessors, lifecycle events
│   ├── mql5_trade_and_positions.md   <- CTrade, CPositionInfo, CSymbolInfo, order execution
│   ├── mql5_indicators_guide.md      <- Buffer indexing, plot styles, iCustom, handles
│   ├── mql5_risk_management.md       <- Dynamic Risk % lot sizing, Trailing Stop, Break-Even
│   ├── mql5_common_errors.md         <- MetaEditor error codes, warnings & repair rules
│   ├── mql5_onnx_ml_guide.md         <- ONNX machine learning model integration
│   └── mql5_opencl_graphics_guide.md <- OpenCL GPU kernels & CCanvas graphics
└── templates/                        <- Production MQL5 Templates (Single Source of Truth)
    ├── ea_template.mq5               <- Production OOP EA template
    ├── indicator_template.mq5        <- Production Custom Indicator template
    └── onnx_ea_template.mq5         <- Production Machine Learning ONNX EA template
```

---

## 3. Workflow Execution Steps

1. **Instant Reference Search**: Query `scripts/search/engine.py` using `uv run python` to fetch exact function signatures and PDF snippets in **< 5 milliseconds**.
2. **Consult Reference Modules**: Inspect applicable markdown reference files in `references/`.
3. **Generate Source Code**: Write clean MQL5 `.mq5` source code based on `templates/`.
4. **Deploy & Compile**: Deploy `.mq5` to MT5 Experts or Indicators folder and run `uv run python scripts/compiler/deployer.py`.
5. **Auto-Repair Verification**: Ensure MetaEditor returns `0 errors, 0 warnings` before presenting final compiled `.ex5` binary to the user.
