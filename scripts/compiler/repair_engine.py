import os
import re
from scripts.compiler.deployer import deploy_and_compile_mql5

COMMON_REPAIRS = [
    (r"implicit conversion from 'number' to 'string'", "Implicit conversion warning fix"),
    (r"not all control paths return a value", "Missing return statement fix"),
    (r"'trade' - struct / class undefined", "Missing #include <Trade\\Trade.mqh> fix")
]

def auto_repair_code(code_text, errors, warnings):
    """Apply common automatic fixes to MQL5 code text based on compiler log."""
    repaired = code_text
    
    # Fix missing include if CTrade used without header
    if any("CTrade" in err or "trade" in err for err in errors):
        if "#include <Trade\\Trade.mqh>" not in repaired:
            repaired = "#include <Trade\\Trade.mqh>\n" + repaired
            
    # Fix missing return in OnInit
    if any("control paths return a value" in err for err in errors):
        if "return(INIT_SUCCEEDED);" not in repaired and "return INIT_SUCCEEDED;" not in repaired:
            repaired = repaired.replace("return;", "return(INIT_SUCCEEDED);")
            
    return repaired

def compile_with_auto_repair(source_file, target_type="strategy", max_retries=2, terminal_base=None, metaeditor_exe=None):
    """Attempt compilation with up to max_retries auto-repair iterations."""
    kw = {}
    if terminal_base: kw["terminal_base"] = terminal_base
    if metaeditor_exe: kw["metaeditor_exe"] = metaeditor_exe
    
    result = deploy_and_compile_mql5(source_file, target_type=target_type, **kw)
    
    retries = 0
    target_path = result.get("target_path", source_file)
    
    while not result["success"] and retries < max_retries:
        retries += 1
        with open(target_path, 'r', encoding='utf-8', errors='ignore') as f:
            code = f.read()
            
        repaired_code = auto_repair_code(code, result["errors"], result["warnings"])
        if repaired_code == code:
            break  # No further automated fixes available
            
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(repaired_code)
            
        result = deploy_and_compile_mql5(target_path, target_type=target_type, **kw)
        
    result["retries"] = retries
    return result
