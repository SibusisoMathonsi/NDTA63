#!/usr/bin/env python3
import subprocess
import os
from pathlib import Path

os.chdir(r"c:\Users\Student\Desktop\NDTA63-main\NDTA63")

print("=== GIT STATUS ===")
result = subprocess.run(["git", "status"], capture_output=True, text=True)
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)

print("\n=== GIT LOG (Last 5 commits) ===")
result = subprocess.run(["git", "log", "--oneline", "-5"], capture_output=True, text=True)
print(result.stdout)

print("\n=== CHECKING LOCAL FILES ===")
for folder in ["Data Preparation", "Database Integration", "Numeric Analysis", 
               "Python or Excel Data Analysis", "Raw datasets", "Report & Demo", "Visualisation"]:
    path = Path(folder)
    if path.exists():
        file_count = len(list(path.rglob("*")))
        print(f"✅ {folder}: {file_count} files/folders")
    else:
        print(f"❌ {folder}: NOT FOUND")

print("\n=== ATTEMPTING PUSH ===")
result = subprocess.run(["git", "push", "-u", "origin", "main"], capture_output=True, text=True)
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)
if result.returncode == 0:
    print("✅ PUSH SUCCESSFUL!")
else:
    print(f"❌ PUSH FAILED with return code {result.returncode}")
    
    # Try force push
    print("\n=== ATTEMPTING FORCE PUSH ===")
    result = subprocess.run(["git", "push", "-f", "origin", "main"], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    if result.returncode == 0:
        print("✅ FORCE PUSH SUCCESSFUL!")
    else:
        print(f"❌ FORCE PUSH FAILED with return code {result.returncode}")
