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

def day_3_task_2():
	# Load input
	input: list[str] = open_file_custom("input3.txt")
	converted_input: list[str] = rows_to_columns(input)

	# List of indexes to remove from each column
	most_index_to_remove: list[int] = []
	least_index_to_remove: list[int] = []

	# Oxygen and CO2 string trackers
	oxygen_string: str = ""
	co2_string: str = ""

	# Loop over each column in the list
	# Each time a number is most/fewest remove the other values from the entry
	for column in converted_input:

		# TODO: Remove this hack and us a proper function
		column: list[int] = [int(x) for x in column]

		# Remove any bad indexes from the column
		most_column: list[int] = [column[x] for x in range(len(column)) if x not in most_index_to_remove]
		least_column: list[int] = [column[x] for x in range(len(column)) if x not in most_index_to_remove]

		# Find most/least common number in column
		most_common_number: int = most_column.count(1) / (len(most_column) / 2)
		least_common_number: int = least_column.count(0) / (len(least_column) / 2)

		# Add value to least/most
		oxygen_string += str(most_common_number)
		co2_string += str(least_common_number)

		# Find positions of most/least common number
		most_bad_entries: list[int] = [x for x in range(len(column)) if most_column[x] == most_common_number]
		least_bad_entries: list[int] = [x for x in range(len(column)) if least_column[x] == least_common_number]

		# Update indexes for next round
		most_index_to_remove.append(most_bad_entries)
		least_index_to_remove.append(least_bad_entries)

		print(f"Column: {list(column)}\n")
		print(f"Most column: {most_column}\n")
		print(f"Most common number: {most_common_number}")
		print(f"Oxygen Rating: {oxygen_string}")
		print(f"Bad entries: {most_bad_entries}\n\n\n")

	# print(f"Task 2 answer: {str(oxygen_string)} , {str(co2_string)}")

	# Convert to decimals
	oxygen: int = int(oxygen_string, 2)
	co2: int = int(co2_string, 2)

	print(f"Oxygen Rating: {oxygen}\nCO2 Rating: {co2}\nLife Support: {oxygen * co2}")

if __name__ == "__main__":
	# day_3_task_1()
	day_3_task_2()
