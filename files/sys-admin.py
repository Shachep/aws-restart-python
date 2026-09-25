import os
import subprocess

# Running a basic system command using os.system
os.system("ls")

# Using subprocess.run to execute shell commands
subprocess.run(["ls"])

# Running command with arguments
subprocess.run(["ls", "-l"])

# Running command with multiple arguments
subprocess.run(["ls", "-l", "README.md"])

# Retrieving system information (uname command)
command = "uname"
commandArgument = "-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])

# Retrieving active process information (ps command)
command = "ps"
commandArgument = "-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])