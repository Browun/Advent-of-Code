def open_file():
    '''
    Reads input from a file address, returning each line as an item
    in a list.
    '''
    with open(f"input{__file__[-4]}.txt", 'r') as in_file:
        content_list = [number.strip() for number in in_file.readlines()]
    return content_list


def day_2_task_1():
	input = open_file()
	# List of integers (horizontal, depth)
	horizontal: int = 0
	vertical: int = 0
	# Add for forward, and down, minus for up
	for n in input:
		direction, value = n.split(" ")
		if direction == "forward":
			horizontal += int(value)
		elif direction == "down":
			vertical += int(value)
		elif direction == "up":
			vertical -= int(value)

	print(f"Task 1: {horizontal * vertical} ({horizontal} * {vertical})\n")

def day_2_task_2():
	input = open_file()
	# List of integers (horizontal, depth)
	horizontal: int = 0
	vertical: int = 0
	aim: int = 0
	# Add for forward, and down, minus for up
	for n in input:
		direction, value = n.split(" ")
		if direction == "forward":
			horizontal += int(value)
			vertical += (aim * int(value))
		elif direction == "down":
			aim += int(value)
		elif direction == "up":
			aim -= int(value)

	print(f"Task 1: {horizontal * vertical} ({horizontal} * {vertical})\n")

if __name__ == "__main__":
	day_2_task_1()
	day_2_task_2()
