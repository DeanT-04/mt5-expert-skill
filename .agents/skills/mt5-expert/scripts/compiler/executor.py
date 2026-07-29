import os
import subprocess
from scripts.config import METAEDITOR_PATH
from scripts.compiler.log_parser import parse_metaeditor_log

def run_metaeditor_compiler(mq5_path, metaeditor_exe=METAEDITOR_PATH, log_path=None):
    """Execute MetaEditor64 CLI compilation in headless mode."""
    if not os.path.exists(metaeditor_exe):
        raise FileNotFoundError(f"MetaEditor executable not found at: {metaeditor_exe}")
    
    if not os.path.exists(mq5_path):
        raise FileNotFoundError(f"MQ5 file not found at: {mq5_path}")
    
    if log_path is None:
        log_path = os.path.splitext(mq5_path)[0] + ".log"
        
    cmd = [metaeditor_exe, f"/compile:{mq5_path}", f"/log:{log_path}"]
    subprocess.run(cmd, capture_output=True, text=True)
    
    log_content = ""
    if os.path.exists(log_path):
        for encoding in ['utf-16', 'utf-8', 'cp1252', 'latin-1']:
            try:
                with open(log_path, 'r', encoding=encoding) as f:
                    log_content = f.read()
                if log_content:
                    break
            except Exception:
                continue
                
    ex5_path = os.path.splitext(mq5_path)[0] + ".ex5"
    success = os.path.exists(ex5_path)
    
    errors, warnings = parse_metaeditor_log(log_content)
    
    return {
        "success": success and (len(errors) == 0),
        "log_content": log_content,
        "errors": errors,
        "warnings": warnings,
        "ex5_path": ex5_path if success else None
    }
