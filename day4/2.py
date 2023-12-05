import time

lines = []
start = time.time()
with open("input.txt",'r') as f:
    lines = f.readlines()

ncards = len(lines)
i=1
for i in range(len(lines)):
    line = lines[i][9:].replace("  ",",").replace(" ",",").replace("\n","")
    split = line.split(",|,")
    win = set(split[0].split(","))
    hand = set(split[1].split(","))
    cardsWon = len(win&hand)
    for j in range(cardsWon):
        for k in range(lines.count(lines[i])):
            lines.append(lines[i+j+1])
    i+=1
end = time.time()
print("time:",end-start)
print(len(lines))
