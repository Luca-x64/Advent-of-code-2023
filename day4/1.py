
lines = []
with open("input.txt",'r') as f:
#with open("input.txt",'r') as f:
    lines = f.readlines()

sum = 0
for i in range(len(lines)):
    line = lines[i][9:].replace("  ",",").replace(" ",",").replace("\n","")
    split = line.split(",|,")
    win = set(split[0].split(","))
    hand = set(split[1].split(","))
    weigth = len(win&hand)
    if weigth != 0:
        sum += 2** (weigth-1)

print(sum)