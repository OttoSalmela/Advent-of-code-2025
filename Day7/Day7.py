def part1():
    with open('input.txt', 'r') as file:
        input = file.read().splitlines()
    
    manifoldMap = []
    for line in input:
        manifoldMap.append(list(line))

    beamIndexs = [manifoldMap[0].index('S')]

    hits = 0
    nextBeamIndexs = []
    for row in manifoldMap[1:]:
        for beam in beamIndexs:
            if row[beam] == '^':
                if beam+1 not in nextBeamIndexs:
                    nextBeamIndexs.append(beam+1)
                if beam-1 not in nextBeamIndexs:
                    nextBeamIndexs.append(beam-1)
                hits += 1
            else:
                if beam not in nextBeamIndexs:
                    nextBeamIndexs.append(beam)
        beamIndexs = nextBeamIndexs
        nextBeamIndexs = []

    print(hits)

#####################################################################################################

if __name__ == "__main__":
    part1()