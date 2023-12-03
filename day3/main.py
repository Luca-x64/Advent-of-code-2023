import re
lines = []



def checkstr(s):
    a = re.sub(r'\.','',s)
    a = re.sub(r'\d','',a)
    print("checkstr",a)
    return len(a) != 0

with open("test.txt",'r') as f:
#with open("input.txt",'r') as f:
    lines = f.readlines()

sum = 0
s=[]

for i in range(len(lines)):
    line = lines[i]
    rightBorder = len(line)
    bottomBorder = len(lines)
    subline=line
    print("line:",i+1,"|",line)

    numeri = re.findall("\d+",line)
    #print("Numeri;",numeri)

    startSub = 0
    for j in range(len(numeri)):
        valid = True
        num = numeri[j]
        
        #Lati
        prima = line[line.index(num)-1: line.index(num) ] #Prima
        
        print("startsub:",startSub)
        print(prima)
        dopo = 0 #Dopo
        if j+1 < len(numeri):
            dopo = line[line.index((numeri[j+1])):line.index((numeri[j+1]))]
        else:
            dopo = line[startSub:startSub+len(num)+1]

        #Line above and below
        aboveSub,belowSub = "",""
        init,end = 0,0
        #left and rigth limit
        if startSub > 0:
                init = len(num)-1
        else:
            init = 0
        
        if startSub == len(line):
            end = len(line)
        else:
            #end = startSub+len(num)+1 -len(num)
            end = startSub+1

        if i != 0: #above
            aboveSub= lines[i-1][init:end]
            
        # print("debug")  
        # print("i",init,end)  
        
        if i+1 < len(lines): #below
            belowSub = lines[i+1][init:end]
        
        
        print("p",num,"d",dopo,"a",aboveSub,"b",belowSub)
        #print(checkstr(aboveSub),checkstr(belowSub) , checkstr(prima) ,checkstr(dopo))
        if checkstr(aboveSub) or checkstr(belowSub) or checkstr(prima) or checkstr(dopo):
            sum += int(num)
            print("sommato")
            s.append(int(num))
        
        startSub+=line.index(num)+len(num)
        print()
        input()
        
print(sum)
print(s)
        #print(checkstr(line))
        # print(prima,num,dopo)    
        # print("a",aboveSub,"b",belowSub)



