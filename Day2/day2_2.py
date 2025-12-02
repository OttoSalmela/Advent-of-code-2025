# read input, remove newlines and split spans into an array
with open('day2.txt', 'r') as file:
    input = file.read().replace('\n','')

spans = input.split(',')

# parse input spans in arrays with min and max of each span
parsedSpans = []
for span in spans:
    parsedSpans.append(span.split('-'))

# loop through values
result = 0
for span in parsedSpans:
    min = span[0]
    max = span[1]

    for value in range(int(min),int(max)+1):
        string = str(value)

        # Concatenate string with itself 
        # Remove first and last characters
        # If original string is in modified string, original string is made of repeating patterns
        if string in (string + string)[1:-1]:
            result += value


print(result)