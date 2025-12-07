import numpy as np

def part1():

    with open('day5.txt', 'r') as file:
        input = [line.strip() for line in file]

    blankIndex = input.index('')
    strFreshRanges = input[:blankIndex]
    availableIds = input[blankIndex+1:]

    freshRanges = []
    for element in strFreshRanges:
            freshRanges.append(element.split('-'))

    ans = 0
    for availableId in availableIds:
            for freshRange in freshRanges:
                    if int(freshRange[0]) <= int(availableId) <= int(freshRange[1]):
                            ans += 1
                            break

    print(ans)

####################################################################################################################

def part2():

    # With help from Akseli Suutari

    with open('input.txt', 'r') as file:
        inputRows = file.read().splitlines()

    # Separate operators
    operators = list(map(str, inputRows[-1].split()))

    # Initialize list for each column of input
    numbers = ['' for _ in range(len(inputRows[0]))]

    # Concate digits from each column to create a list of actual numbers
    for ii in range(len(inputRows)-1):
        for jj in range(len(inputRows[ii])):
            numbers[jj] += inputRows[ii][jj].strip()


    # Go through list of actual numbers and add them to "terms" array.
    # If item in number list is not numeric or is the last one, perform calculation according to current operator and add to ans.
    # Empty terms array, change to next operator and start again.        
    ans = 0
    terms = []
    operatorsCounter = 0
    for ii in range(len(numbers)):
        if numbers[ii].isnumeric():
            terms.append(int(numbers[ii]))
        if not numbers[ii].isnumeric() or ii == len(numbers)-1:
            if operators[operatorsCounter] == '+':
                ans += sum(terms)
            if operators[operatorsCounter] == '*':
                ans += np.prod(terms)
            operatorsCounter += 1
            terms = []
            

    print(ans)

########################################################################################################################

if __name__ == "__main__":
    part2()