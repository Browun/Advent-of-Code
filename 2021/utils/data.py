def rows_to_columns(data: list[str]) -> list[str]:
	'''Transpose a list of strings.'''

	# Create output list
	output: list[str] = []

	# Length of entry, assuming consistency across list
	data_length: int = len(data) - 1
	value_length: int = len(data[0])

	# For every value in an entry
	for value_index in range(value_length):
		output.append('')

		# For every value in the data
		for data_index in range(data_length):
			# print(f"Data index: {data_index}\nData value: {data[data_index]}\nValue index: {value_index}")

			# For current data index, add the entry at value index
			output[-1] += data[data_index][value_index]

		# print(f"Index: {value_index}\nLatest value: {output[-1]}")

	return output
