
def getAdjacentCoordinates(x,y,xMax,yMax):
    adjacent = []
    for jj in range(y-1,y+2):
          if jj < 0 or jj > yMax-1:
                continue
          else:
                for ii in range(x-1,x+2):
                      if ii < 0 or ii > xMax-1 or (ii == x and jj == y):
                            continue
                      else:
                            adjacent.append([ii,jj])
    return adjacent

def countRolls(grid,coordinates):
    count = 0
    for coordinate in coordinates:
          if grid[coordinate[0]][coordinate[1]] == '@':
                count += 1
    return count
            

if __name__ == "__main__":

    with open('day4.txt', 'r') as file:
            input = [line.strip() for line in file]

    grid = []
    for row in input:
          grid.append(list(row))
    
    yMax = len(grid)
    xMax = len(grid[0])

    res = 0
    while True:
        loopRes = 0
        for x in range (0,xMax):
            for y in range(0,yMax):
                    if grid[x][y] != '@':
                        continue
                    adjacentCoordinates = getAdjacentCoordinates(x,y,xMax,yMax)
                    if countRolls(grid,adjacentCoordinates) < 4:
                        grid[x][y] = '.'
                        loopRes += 1 
        if loopRes == 0:
              break
        else:
            res += loopRes

    
    print(res)
    

