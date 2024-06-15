import os
import sys

cmd=f"python3 src/main.py {sys.argv[1]}"

print(f"Running Command: {cmd}")
os.system(cmd)
