"""

"""

import math


# Add any extra import statements you may need here


# Add any helper functions you may need here


def canGetExactChange(targetMoney, denominations):
    sorted_denominations = sorted(denominations)
    sorted_denominations.reverse() #Sort array and organize highest denominations first
    return exactChange(targetMoney, sorted_denominations) #Call recursive function

def exactChange(money, denominations):
    if money == 0: #If the money was divisible to exactly zero, horray we have a solution.
        return True #Ripple up 'True' through the recursive functions. See lines 25 & 27.
    if money < 0:    #If the denomination overshot (e.g. not divisible), terminate the current
        return False #iteration of the recursive function, move on to the next denomination.
    for denom in denominations: #For each denomination...
        if(exactChange(money-denom, denominations)): #Subtract the temporary money value by the current denomination.
            #print(denom) #Uncomment to view the recursive solution.
            return True
    return False #If we hit this part of the code, no combination of denominations worked (in
                 #the current tree). Thus, return False.

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

    target_4 = 1298
    arr_4 = [8, 14, 29, 45, 56, 121]
    expected_4 = True
    output_4 = canGetExactChange(target_4, arr_4)
    check(expected_4, output_4)
    # Add your own test cases here
