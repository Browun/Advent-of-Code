import re
import fileinput

# 1000 x 1000
# ID @ L,T: WxH
# L and T define spaces from left/above the cut

# generate list for numbers in the area of cloth i.e. 1, 2, 3, 4, etc.
# for each suggestion
#  - generate area covered (list comprehension)
#  - check for value presence in list
#  - +1 to all values on the fabric


def return_dimensions(fabric_height, fabric_width, fabric_value):
    '''
    Transforms the input in to list of the correct dimensions, where each cell is has a unique
    number, on the value range of 0 to n, whereby n = (fabric height * fabric_width).

    :NOTE: The range is inclusive of 0
    '''

    return fabric_value * fabric_height * fabric_width


def elf_suggestions(suggestion, fabric_width, fabric):
    '''
    For every elf suggestion of the fabric cut, extract values, calculate the area it covers, 
    and look for these values in the fabric, if present remove, else plus one to the 
    number_of_multiple_claims
    '''
    pattern = r'(#\d+) @ (\d+),(\d+): (\d+)x(\d+)'
    re_match = re.match(pattern=pattern, string=suggestion)
    uid, from_left, from_top, width, height = re_match.groups()

    from_left = int(from_left)
    from_top = int(from_top)
    width = int(width)
    height = int(height)


    for row in range(height):
        # Check for each row from the given starting position
        # Equation accounts for the donimanation used for splitting up the rows
        starting_position = ((from_top + row) * fabric_width) + from_left

        for value in range(starting_position, starting_position + width):
            # Check for each value from the given starting position, iterating columns
                fabric[value] += 1

    return fabric



def part_1(fabric_height=1000, fabric_width=1000, fabric_value=[0]):
    '''
    Function to run part 1 of the task.
    '''

    input_file = 'day-3/aoc-day3-input.txt'

    with open(input_file, 'r') as in_file:
        file = in_file.read()
        content_list = list(file.split('\n'))
        fabric = return_dimensions(fabric_height=fabric_height, fabric_width=fabric_width, fabric_value=fabric_value)

        for suggestion in content_list:
            fabric = elf_suggestions(suggestion=suggestion, fabric_width=fabric_width, fabric=fabric)

        number_of_mutliple_claims = sum(n >= 2 for n in fabric)

    return number_of_mutliple_claims


def part_2(fabric_height, fabric_width, fabric_value=list()):
    '''
    Function to run part 2 of the task.
    '''
    input_file = 'day-3/aoc-day3-input.txt'
    uid_set = set()
    intersection = set()
    fabric = [ [] for number in range(fabric_width * fabric_height)]

    for suggestion in fileinput.input(input_file):
        pattern = r'(#\d+) @ (\d+),(\d+): (\d+)x(\d+)'
        re_match = re.match(pattern=pattern, string=suggestion)
        uid, from_left, from_top, width, height = re_match.groups()

        uid_set.add(uid)
        from_left = int(from_left)
        from_top = int(from_top)
        width = int(width)
        height = int(height)


        for row in range(height):
            # Check for each row from the given starting position
            # Equation accounts for the donimanation used for splitting up the rows
            starting_position = ((from_top + row) * fabric_width) + from_left

            for value in range(starting_position, starting_position + width):
                # Check for each value from the given starting position, iterating columns
                    if fabric[value] and uid not in fabric[value]:
                        # If the list is not empty, and the uid isn't already in this cell
                        intersection.add(uid)   # Add the uid to this list
                        intersection.update(fabric[value])   # Update the values from this cell in to the set
                    fabric[value].append(uid)   # Add the uid to this list

    return (uid_set - intersection).pop()

if __name__ == '__main__':
    fabric_height = 1000
    fabric_width = 1000
    print(
          part_1(fabric_height=fabric_height, 
               fabric_width=fabric_width),
          part_2(fabric_height=fabric_height,
                fabric_width=fabric_width,
                fabric_value=list())
          )