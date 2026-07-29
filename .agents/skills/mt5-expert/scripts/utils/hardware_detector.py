import os
import subprocess
import json
import platform

def detect_cpu_specs():
    """Detect CPU physical cores and logical processors."""
    logical = os.cpu_count() or 4
    physical = max(1, logical // 2)
    cpu_name = platform.processor() or "Generic CPU"
    
    if platform.system() == "Windows":
        try:
            cmd = ["powershell", "-Command", "Get-CimInstance Win32_Processor | Select-Object Name, NumberOfCores, NumberOfLogicalProcessors | ConvertTo-Json"]
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=3)
            if res.returncode == 0 and res.stdout.strip():
                data = json.loads(res.stdout)
                if isinstance(data, list):
                    data = data[0]
                cpu_name = data.get("Name", cpu_name)
                physical = data.get("NumberOfCores", physical)
                logical = data.get("NumberOfLogicalProcessors", logical)
        except Exception:
            pass
            
    return {
        "name": cpu_name,
        "physical_cores": physical,
        "logical_cpus": logical
    }

def detect_gpu_specs():
    """Detect GPU hardware acceleration device names."""
    gpus = []
    if platform.system() == "Windows":
        try:
            cmd = ["powershell", "-Command", "Get-CimInstance Win32_VideoController | Select-Object Name | ConvertTo-Json"]
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=3)
            if res.returncode == 0 and res.stdout.strip():
                data = json.loads(res.stdout)
                if isinstance(data, list):
                    gpus = [item.get("Name") for item in data if item.get("Name")]
                elif isinstance(data, dict):
                    gpus = [data.get("Name")]
        except Exception:
            pass
            
    if not gpus:
        gpus = ["Integrated / Standard Display Controller"]
        
    return gpus

def auto_detect_hardware():
    """Detect full hardware profile and auto-calculate optimal parallel threads."""
    cpu = detect_cpu_specs()
    gpus = detect_gpu_specs()
    
    logical = cpu["logical_cpus"]
    
    # Auto-threads rule: Maximize throughput without locking OS
    if logical <= 4:
        optimal_threads = logical
    elif logical <= 8:
        optimal_threads = logical
    else:
        optimal_threads = min(32, int(logical * 1.5))
        
    return {
        "cpu_name": cpu["name"],
        "physical_cores": cpu["physical_cores"],
        "logical_cpus": cpu["logical_cpus"],
        "gpus": gpus,
        "optimal_threads": optimal_threads
    }

if __name__ == "__main__":
    hw = auto_detect_hardware()
    print("=" * 60)
    print("SMART HARDWARE DETECTOR")
    print("=" * 60)
    print(f"CPU: {hw['cpu_name']}")
    print(f"Physical Cores: {hw['physical_cores']} | Logical CPUs: {hw['logical_cpus']}")
    print(f"Detected GPU(s): {', '.join(hw['gpus'])}")
    print(f"Auto-Selected Parallel Worker Threads: {hw['optimal_threads']}")
    print("=" * 60)
