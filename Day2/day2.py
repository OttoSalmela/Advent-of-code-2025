# read input, remove newlines and split spans into an array
with open('day2.txt', 'r') as file:
    input = file.read().replace('\n','')

spans = input.split(',')

# parse input spans in arrays with min and max of each span
parsedspans = []
for span in spans:
    parsedspans.append(span.split('-'))

# loop through values and evaluate if second half of value is same as first half
result = 0
for span in parsedspans:
    min = span[0]
    max = span[1]

    for value in range(int(min),int(max)+1):
        string = str(value)
        length = len(string)
        firstHalf = string[:length//2 + length%2]
        secondHalf = string[length//2 + length%2:]
        if firstHalf == secondHalf:
            result += value

print(result)