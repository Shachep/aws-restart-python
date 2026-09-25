import os
import subprocess

# Running a basic bash command using os.system
os.system("ls")

# Running a command and capturing output using subprocess.run
subprocess.run(["ls", "-l"])

# Retrieving system information
subprocess.run(["uname", "-a"])

# Checking active processes
subprocess.run(["ps", "-x"])