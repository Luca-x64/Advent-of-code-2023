import re
lines = []

def checkstr(s):
    a = re.findall('\d',s)
    return len(a) != 0

#with open("test.txt",'r') as f:
with open("input.txt",'r') as f:
    lines = f.readlines()

sum = 0
for i in range(len(lines)):
    line = lines[i]
    numeri = re.findall("[*]",line)
    print(numeri)
    

    startSub = 0
    for num in numeri:
        leftIndex = startSub+ line[startSub:].index(num)        
        #Left
        prima = 0 
        if leftIndex != 0:
            prima = line[leftIndex-1:leftIndex] 
        else: #leftIndex = 0
            prima = ""
            leftIndex=0
        
        #Right
        dopo = 0 
        rightIndex = leftIndex+1+len(num)
        if rightIndex == len(line):
            dopo = ""
        else:
            dopo = line[rightIndex-1:rightIndex]
            rightIndex = rightIndex+1
        
        #Line above and below
        aboveSub,belowSub = "",""
        #Above
        if i != 0:
            if leftIndex == 0:
                aboveSub= lines[i-1][leftIndex:rightIndex-1]
            else:    
                aboveSub= lines[i-1][leftIndex-1:rightIndex-1]
        
        #Below
        if i+1 < len(lines):
            if leftIndex == 0:
                belowSub = lines[i+1][leftIndex:rightIndex-1]
            else:
                belowSub = lines[i+1][leftIndex-1:rightIndex-1]
                print("c",leftIndex-1)
                print("b",lines[i+1][:leftIndex-1])
                print("a",re.findall('\d+',line[i+1][:leftIndex-1:-1]))
            
            side = [checkstr(aboveSub), checkstr(belowSub), checkstr(prima), checkstr(dopo)]


        print(prima,dopo,aboveSub,belowSub)
        if side.count(True) >=2 :
            pass
            #sum += int(num)
        
        startSub= rightIndex - 1
        
print(sum)