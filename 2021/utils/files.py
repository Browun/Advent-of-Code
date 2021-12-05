def open_file(input_file):
    '''
    Reads input from a file address, returning each line as an item
    in a list.
    '''
    with open(input_file, 'r') as in_file:
        file = in_file.read()
        content_list = list(file.split('\n'))
    return content_list