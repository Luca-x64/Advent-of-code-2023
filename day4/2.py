import time
lines = []
with open("input.txt",'r') as f:
    lines = f.readlines()

ncards = len(lines)
print(ncards)

i=1
a = time.now()
for i in range(len(lines)):
    line = lines[i][9:].replace("  ",",").replace(" ",",").replace("\n","")
    split = line.split(",|,")
    win = set(split[0].split(","))
    hand = set(split[1].split(","))
    cardsWon = len(win&hand)
    print(cardsWon)
    for j in range(cardsWon):
        for k in range(lines.count(lines[i])):
            lines.append(lines[i+j+1])
    i+=1
    
b = time.now()
print(b-a)
print(len(lines))
