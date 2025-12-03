def maxCharInLine(line):
    maxValue = 0
    maxIndex = 0
    for ii in range(len(line)):
            if int(line[ii]) > maxValue:
                maxValue = int(line[ii])
                maxIndex = ii
    return maxValue, maxIndex

def findJoltage(line,n,ans=''):  
    if len(ans) == 11:
        maxValue, maxIndex = maxCharInLine(line)
        ans += str(maxValue)
        return int(ans)
    else:
        line = line.rstrip('\n')
        maxValue, maxIndex = maxCharInLine(line[:len(line)-n])
        ans += str(maxValue)
        ans = findJoltage(line[maxIndex+1:],n-1,ans)
        return(ans)
        
        
        

    


if __name__ == "__main__":

    file = open('day3.txt', 'r')
    lines = file.readlines()

    numberOfDigits = 12

    total = 0
    for line in lines:
       joltage = findJoltage(line,numberOfDigits-1)
       total += joltage

    
    print(total)
