"""

"""

import math


# Add any extra import statements you may need here


# Add any helper functions you may need here

def canGetExactChange(targetMoney, denominations):

# Write your code here

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printString(string):
    print('[\"', string, '\"]', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    target_1 = 94
    arr_1 = [5, 10, 25, 100, 200]
    expected_1 = False
    output_1 = canGetExactChange(target_1, arr_1)
    check(expected_1, output_1)

    target_2 = 75
    arr_2 = [4, 17, 29]
    expected_2 = True
    output_2 = canGetExactChange(target_2, arr_2)
    check(expected_2, output_2)

    target_3 = 67
    arr_3 = [4, 17, 29]
    expected_3 = True
    output_3 = canGetExactChange(target_3, arr_3)
    check(expected_3, output_3)

    target_4 = 130
    arr_4 = [7, 15, 28, 56, 121]
    expected_4 = True
    output_4 = canGetExactChange(target_4, arr_4)
    check(expected_4, output_4)

    target_5 = 61
    arr_5 = [7, 17, 29]
    expected_5 = False
    output_5 = canGetExactChange(target_5, arr_5)
    check(expected_5, output_5)
           
    # Add your own test cases here
