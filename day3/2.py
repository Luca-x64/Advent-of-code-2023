import re
lines = []

def checkstr(s):
    a = re.findall('\d',s)
    return len(a) != 0

with open("test.txt",'r') as f:
#with open("input.txt",'r') as f:
    lines = f.readlines()

sum = 0
for i in range(len(lines)):
    line = lines[i]
    numeri = re.findall("[*]",line)
    
    nearNumbers = []
    startSub = 0
    for num in numeri:
        leftIndex = startSub+ line[startSub:].index(num)      
        print("leftIndex:",leftIndex)  
        #Left

        prima = line[max([leftIndex-1,0]):leftIndex] 
        
        #Right
        dopo = 0 
        rightIndex = leftIndex+1+len(num)
        if rightIndex != len(line):
            rightIndex = rightIndex+1
        
        dopo = line[rightIndex-1:min([rightIndex,len(line)])]
        
        #Line above and below
        aboveSub,belowSub = "",""

        #Above
        if i != 0:    
            fix=0
            if lines[i-1][leftIndex]==".":
                fix = 1

            aboveSub= lines[i-1][max([leftIndex-1,0]):rightIndex-1]
            
            sidesx = "."+lines[i-1][max([0,leftIndex-3]):leftIndex]
            sidedx = lines[i-1][leftIndex +fix :min([len(line), leftIndex+fix+4])]+"."
            #print(sidesx,sidedx)
            b = lines[i-1][max([0,leftIndex-3]):min([leftIndex+4+fix,len(lines[i-1])])]
            print("B",b)

            
            if lines[i-1][leftIndex]==".":
                left = b[:line[startSub:].index(num)]
                right = b[:leftIndex]
                print("left",left)
                print("right",right)
            else:
                aboveNum = b[sidesx.rfind("."): leftIndex+fix+ sidedx.find(".")].replace(".","")
                print(aboveNum)
            print(nearNumbers)
        #Below
        if i+1 < len(lines):
    
            fix=0
            if lines[i-1][leftIndex]==".":
                fix = 1
            belowSub = lines[i+1][max([leftIndex-1,0]):rightIndex-1]

            sidesx = "."+lines[i+1][max([0,leftIndex-3]):leftIndex]
            sidedx = lines[i+1][leftIndex +fix :min([len(line), leftIndex+fix+4])]+"."
        
            b = lines[i+1][max([0,leftIndex-3]):min([leftIndex+4+fix,len(line)])]
            belowNum = b[sidesx.rfind("."): leftIndex+fix+ sidedx.find(".")].replace(".","")
        #print(aboveNum,belowNum)
        side = [checkstr(aboveSub), checkstr(belowSub), checkstr(prima), checkstr(dopo)]
        input()

        print(prima,dopo,aboveSub,belowSub)
        if side.count(True) ==2 :
            pass
            #sum += int(num)
        
        startSub= rightIndex - 1
        
print(sum)