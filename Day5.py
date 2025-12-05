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

#################################################################################################################################################################################

def part2():
    with open('day5.txt', 'r') as file:
        input = [line.strip() for line in file]

    blankIndex = input.index('')
    strFreshRanges = input[:blankIndex]

    freshRanges = []
    for element in strFreshRanges:
            minimum, maximum = element.split('-')
            freshRanges.append([int(minimum),int(maximum)])

    sortedRanges = sorted(freshRanges, key=lambda x: x)

    mergedRanges = []
    mergedRanges.append(sortedRanges[0])

    for ii in range(1,len(sortedRanges)):
        current = sortedRanges[ii]

        if current[0] <= mergedRanges[-1][1]:
            mergedRanges[-1][1] = max(mergedRanges[-1][1],current[1])
        else:
            mergedRanges.append(current)

    ans = 0
    for element in mergedRanges:
          ans += element[1]-element[0]+1

    print(ans)
#################################################################################################################################################################################

if __name__ == "__main__":
    part1()
    part2()
