def letter_repeat():
    input_file = 'aoc-day2.1-input.txt'
    output_file = 'aoc-day2.1-output.txt'

    with open(input_file, 'r') as in_file:
        file = in_file.read()
        letter_set = set((file.split('\n')))

        # Test cases
        # letter_set = set(['aba', 'ab', 'abc', 'abb', 'abbb', 'abbc'])
        # letter_set = set(['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab'])

        two_letter_list = list(([0] * len(letter_set)))
        three_letter_list = list(([0] * len(letter_set)))

        for k, box_ID in enumerate(letter_set):
            for letter in box_ID:
                if box_ID.count(letter) > 1:

                    if box_ID.count(letter) == 2:
                        two_letter_list[k] = 1

                    if box_ID.count(letter) == 3:
                        three_letter_list[k] = 1

                else:
                    pass

        in_file.close()

    with open(output_file, 'w') as out_file:
        two_letter_sum = sum(two_letter_list)
        three_letter_sum = sum(three_letter_list)
        answer = two_letter_sum * three_letter_sum
        out_file.write(str(answer))
        out_file.close()

    return


if __name__ == '__main__':
    letter_repeat()
