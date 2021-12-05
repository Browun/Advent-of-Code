#!/usr/bin/env python3

from utils.files import open_file_custom
from utils.data import rows_to_columns

def day_3_task_1():
	# Load input
	input: list[str] = open_file_custom("input3.txt")
	converted_input = rows_to_columns(input)

	# Produce gamma and epsilon values
	gamma_string: str = ''.join(['1' if x.count("1") > (len(x) / 2) else '0' for x in converted_input])
	gamma: int = int(gamma_string, 2)
	epsilon_string: str = ''.join(['1' if x == '0' else '0' for x in gamma_string])
	epsilon: int = int(epsilon_string, 2)

	# Return gamma * epsilon
	print(f"Gamma: {gamma}\nEpsilon: {epsilon}\nMultiplied: {gamma * epsilon}")

if __name__ == "__main__":
	day_3_task_1()
