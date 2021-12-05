
def open_file():
    '''
    Reads input from a file address, returning each line as an item
    in a list.
    '''
    with open(f"input{__file__[-4]}.txt", 'r') as in_file:
        content_list = [int(number.strip()) for number in in_file.readlines()]
    return content_list

def day_1_task_1():
	input_list: list[str] = open_file()
	answer_1: int = sum([1 for i in range(1, len(input_list)) if input_list[i] > input_list[i-1]])
	print(f"Task 1: {answer_1}\n")

def day_2_task_2():
	input_list: list[str] = open_file()
	answer_2: int = sum([1 for i in range(3, len(input_list)) if input_list[i] > input_list[i-3]])
	print(f"Task 2: {answer_2}\n")

if __name__ == '__main__':
	day_1_task_1()
	day_2_task_2()
