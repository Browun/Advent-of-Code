def open_file_custom(input_file: str) -> list[str]:
    '''
    Reads input from a file address, returning each line as an item
    in a list.
    '''
    with open(input_file, 'r') as in_file:
        file = in_file.read()
        content_list: list[str] = list(file.split('\n'))

    return content_list

def open_file() -> list[str]:
    '''
    Reads input from a file address, returning each line as an item
    in a list.
    '''
    with open(f"input{__file__[-4]}.txt", 'r') as in_file:
        content_list: list[str] = [number.strip() for number in in_file.readlines()]
    return content_list
