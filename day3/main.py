import re
lines = []
with open("test.txt",'r') as f:
#with open("input.txt",'r') as f:
    lines = f.readlines()

sum = 0

for i in range(len(lines)):
    line = lines[i]
    rightBorder = len(line)
    bottomBorder = len(lines)
    subline=line


    numeri = re.findall("\d+",line)
    startSub = 0

    for j in range(len(numeri)):
        valid = True
        num = numeri[j]
        
        #Lati
        prima = line[startSub: line.index(num) ] #Prima
        startSub+=len(prima)+len(num)
        
        dopo = 0 #Dopo
        if j+1 < len(numeri):
            dopo = line[startSub:line.index((numeri[j+1]))]
        else:
            dopo = line[startSub:]

        #Line above and below
        input()
    