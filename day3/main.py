import re
lines = []



def checkstr(s):
    a = re.sub(r'\.','',line)
    print("AA",a)
    return len(a) == 0

#with open("test.txt",'r') as f:
with open("input.txt",'r') as f:
    lines = f.readlines()

sum = 0

for i in range(len(lines)):
    line = lines[i]
    rightBorder = len(line)
    bottomBorder = len(lines)
    subline=line
    #print("line:",i+1)

    numeri = re.findall("\d+",line)
    #print("Numeri;",numeri)

    for j in range(len(numeri)):
        startSub = 0
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
        aboveSub,belowSub = 0,0
        init,end = 0,0
        #left and rigth limit
        if startSub > 0:
                init = startSub-1-len(num)
        else:
            init = 0

        if startSub == len(line):
            end = len(line)
        else:
            end = startSub+len(num)+1 -len(num)

        if i != 0: #above
            aboveSub= lines[i-1][init:end]
            
        # print("debug")  
        # print("i",init,end)  
        
        if i+1 < len(lines): #below
            belowSub = lines[i+1][init:end]
        print(line)
        print(aboveSub)
        print(checkstr(aboveSub))
        input()
        #print(checkstr(line))
        # print(prima,num,dopo)    
        # print("a",aboveSub,"b",belowSub)



