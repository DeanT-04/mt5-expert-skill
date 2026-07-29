import os
import shutil
from scripts.config import EXPERTS_DIR, INDICATORS_DIR, DEFAULT_TERMINAL_BASE, METAEDITOR_PATH
from scripts.compiler.executor import run_metaeditor_compiler

def deploy_and_compile_mql5(source_file, target_type="strategy", custom_name=None, terminal_base=DEFAULT_TERMINAL_BASE, metaeditor_exe=METAEDITOR_PATH):
    """Deploy .mq5 file to MT5 Experts or Indicators folder and run MetaEditor compilation."""
    filename = os.path.basename(source_file)
    if custom_name:
        if not custom_name.endswith(".mq5"):
            custom_name += ".mq5"
        filename = custom_name
        
    t_type = target_type.lower()
    if t_type in ['s', 'ea', 'strategy', 'expert']:
        dest_dir = os.path.join(terminal_base, "Experts")
    elif t_type in ['i', 'indicator']:
        dest_dir = os.path.join(terminal_base, "Indicators")
    else:
        raise ValueError(f"Unknown target type: {target_type}. Use 'strategy' or 'indicator'.")
        
    os.makedirs(dest_dir, exist_ok=True)
    target_path = os.path.join(dest_dir, filename)
    
    shutil.copy2(source_file, target_path)
    
    res = run_metaeditor_compiler(target_path, metaeditor_exe=metaeditor_exe)
    res["target_path"] = target_path
    
    return res
