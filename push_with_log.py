#!/usr/bin/env python3
import subprocess
import os
from pathlib import Path

os.chdir(r"c:\Users\Student\Desktop\NDTA63-main\NDTA63")

output = []

def run_cmd(cmd_list, label):
    output.append(f"\n{'='*60}")
    output.append(f"COMMAND: {' '.join(cmd_list)}")
    output.append(f"LABEL: {label}")
    output.append('='*60)
    
    try:
        result = subprocess.run(
            cmd_list,
            capture_output=True,
            text=True,
            timeout=60
        )
        output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        output.append(f"Return Code: {result.returncode}")
    except Exception as e:
        output.append(f"EXCEPTION: {type(e).__name__}: {e}")

# Run commands
run_cmd(["git", "status"], "Check git status")
run_cmd(["git", "log", "--oneline", "-5"], "Check commit history")
run_cmd(["git", "add", "."], "Stage all files")
run_cmd(["git", "status"], "Status after add")
run_cmd(["git", "commit", "-m", "Push all Data Analytics project content"], "Create commit")
run_cmd(["git", "log", "--oneline", "-5"], "Check commits after commit")
run_cmd(["git", "push", "-v", "origin", "main"], "Push to GitHub with verbose output")
run_cmd(["git", "status"], "Final status")

# Write output to file
output_file = Path(r"c:\Users\Student\Desktop\NDTA63-main\NDTA63\GIT_PUSH_LOG.txt")
with open(output_file, 'w') as f:
    f.write('\n'.join(output))

print(f"Output written to: {output_file}")
for line in output[-30:]:  # Print last 30 lines
    print(line)
