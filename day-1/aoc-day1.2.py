# TODO: Investigate utilising set objects instead to speed up the search


def frequnecy_repeat():
    input_file = 'aoc-day1-input.txt'
    output_file = 'aoc-day1.2-output.txt'
    base_frequency = 0
    frequency_list = [0]
    found_number = False

    with open(input_file, 'r') as in_file:
        file = in_file.read()
        number_set = set((file.split('\n')))

        # Test cases
        # number_list = ['+1', '-1']
        # number_list = ['+3', '+3', '+4', '-2', '-4']
        # number_list = [-6, +3, +8, +5, -6]
        # number_list = [+7, +7, -2, -7, -4]

        while found_number is False:
            for number in number_set:
                base_frequency += int(number)

                if base_frequency in frequency_list:
                    print(base_frequency)
                    print('DONE')
                    found_number = True
                    in_file.close()
                    break

                else:
                    frequency_list.append(base_frequency)

    with open(output_file, 'w') as out_file:
        out_file.write(str(base_frequency))
        out_file.close()

    return


if __name__ == '__main__':
    frequnecy_repeat()
