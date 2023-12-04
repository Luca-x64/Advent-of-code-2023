lines = []
with open("input.txt",'r') as f:
    lines = f.readlines()

occurrencies = []
ncards = len(lines)
print(ncards)
i=1
for i in range(len(lines)):
#while i < len(lines):
    line = lines[i][9:].replace("  ",",").replace(" ",",").replace("\n","")
    split = line.split(",|,")
    win = set(split[0].split(","))
    hand = set(split[1].split(","))
    cardsWon = len(win&hand)
    occurrencies.append(cardsWon)
    #for j in range(cardsWon):
    #    lines.append(lines[i+j+1])
    #i+=1

print(ncards)
