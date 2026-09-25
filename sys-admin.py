import os
import subprocess

# Exercise 1: Using os.system to run 'ls'
print("--- Exercise 1: os.system ---")
os.system("ls")

# Exercise 2: Using subprocess.run with a list
print("\n--- Exercise 2: subprocess.run(['ls']) ---")
subprocess.run(["ls"])

# Exercise 3: Using subprocess.run with two arguments ('ls', '-l')
print("\n--- Exercise 3: subprocess.run(['ls', '-l']) ---")
subprocess.run(["ls", "-l"])

# Exercise 4: Using subprocess.run with three arguments ('ls', '-l', 'README.md')
print("\n--- Exercise 4: subprocess.run with file argument ---")
subprocess.run(["ls", "-l", "README.md"])

# Exercise 5: Retrieving system information with 'uname -a'
command = "uname"
commandArgument = "-a"
print(f'\n--- Exercise 5: Gathering system information with command: {command} {commandArgument} ---')
subprocess.run([command, commandArgument])

# Exercise 6: Retrieving active process information with 'ps -x'
command = "ps"
commandArgument = "-x"
print(f'\n--- Exercise 6: Gathering active process information with command: {command} {commandArgument} ---')
subprocess.run([command, commandArgument])