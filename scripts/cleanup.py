#!/usr/bin/env python3
"""ZeroPoint Cleanup Utility"""

import os
import shutil
import glob

def cleanup():
    """Clean up temporary files and logs"""
    cleanup_patterns = [
        "*.pyc",
        "__pycache__/",
        "*.log",
        "temp/",
        "sessions/"
    ]
    
    print("[*] Starting cleanup...")
    
    for pattern in cleanup_patterns:
        files = glob.glob(pattern, recursive=True)
        for file in files:
            try:
                if os.path.isdir(file):
                    shutil.rmtree(file)
                else:
                    os.remove(file)
                print(f"[+] Removed: {file}")
            except Exception as e:
                print(f"[-] Failed to remove {file}: {e}")
    
    print("[*] Cleanup complete!")

if __name__ == "__main__":
    cleanup()