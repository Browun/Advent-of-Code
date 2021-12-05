import sys
import os
import subprocess

# TODO: Make the challenges run from this main file

# Input arguments for process
input_arguments = sys.argv[1:]
cwd = os.curdir
my_env = os.environ.copy()

# Set variables from input arguments, or break if missing arguments
if len(input_arguments) != 3:
	print("Three arguments are needed to run this file:\nyear (yyyy)\nday (d)\ntask (1 or 2)")
	exit(1)
else:
	year, day, task = input_arguments
	print(f"\nRunning for inputs:\nYear: {year}\nDay: {day}\nTask: {task}\n")

# Run the relevant file based on the inputs
arguments = ["python", f"{cwd}/{year}/day-{day}/day-{task}.py"]

# Begin the relevant subprocess
process = subprocess.run(args=arguments, capture_output=True, timeout=120.0, cwd=cwd, env=my_env)

# Print standard output if successfully processed, otherwise return standard error
if process.returncode == 0:
	print(process.stdout)
else:
	print(process.stderr)
