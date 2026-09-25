import os
import subprocess

# Exercise 1: Using os.system to run 'ls'
print("--- Using os.system ---")
os.system("ls")

# Exercise 2: Using subprocess.run to run ['ls']
print("\n--- Using subprocess.run with one argument ---")
subprocess.run(["ls"])

# Exercise 3: Using subprocess.run with two arguments (long listing format)
print("\n--- Using subprocess.run with two arguments (ls -l) ---")
subprocess.run(["ls", "-l"])

# Exercise 4: Using subprocess.run with three arguments (inspecting README.md)
print("\n--- Using subprocess.run with three arguments (ls -l README.md) ---")
subprocess.run(["ls", "-l", "README.md"])

# Exercise 5: Retrieving system information with 'uname -a'
command = "uname"
commandArgument = "-a"
print(f'\nGathering system information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])

# Exercise 6: Retrieving active process information with 'ps -x'
command = "ps"
commandArgument = "-x"
print(f'\nGathering active process information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])