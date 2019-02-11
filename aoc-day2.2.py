def remove_character(string, index):
    if index == 0:
        new_string = string[1:]
        return new_string

    elif index == len(string):
        new_string = string[:index - 1]
        return new_string

    else:
        new_string = string[:index] + string[index + 1:]
        return new_string


def id_check():
    input_file = 'aoc-day2-input.txt'
    output_file = 'aoc-day2.2-output.txt'

    with open(input_file, 'r') as in_file:
        file = in_file.read()
        id_list = list(file.split('\n'))

    edited_id_list = id_list.copy()

    for id in id_list:
        primary_id = edited_id_list.pop(edited_id_list.index(id))

        for letter_index, letter in enumerate(primary_id):
            primary_id_edit = remove_character(primary_id, letter_index)

            for secondary_id in edited_id_list:
                secondary_id_edit = remove_character(secondary_id, letter_index)

                if primary_id_edit == secondary_id_edit:
                    with open(output_file, 'w') as out_file:
                        out_file.write(primary_id_edit)
                        out_file.close()
                        return


if __name__ == '__main__':
    id_check()
