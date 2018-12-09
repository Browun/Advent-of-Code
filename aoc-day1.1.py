def frequency_change():
    input_file = 'aoc-day1.1-input.txt'
    output_file = 'aoc-day1.1-output.txt'
    base_frequency = 0

    with open(input_file, 'r') as in_file:
        file = in_file.read()
        number_list = file.split('\n')
        for number in number_list:
            base_frequency += int(number)
        in_file.close()

    with open(output_file, 'w') as out_file:
        out_file.write(str(base_frequency))
        out_file.close()

    return


if __name__ == '__main__':
    frequency_change()
