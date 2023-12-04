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
    lines[i] = re.sub(r'[^0-9.*]','.', lines[i])
    line = lines[i]
    print("line,",i)
    numeri = re.findall("[*]",line)
    
    nearNumbers = []
    startSub = 0
    cnt = 0
    for num in numeri:
        leftIndex = startSub+ line[startSub:].index(num)
        
        #Left
        prima = line[max([leftIndex-3,0]):leftIndex] 
        #Right
        dopo = 0 
        rightIndex = leftIndex+1+len(num)
        if rightIndex != len(line):
            rightIndex = rightIndex+1
        
        dopo = line[rightIndex-1:min([rightIndex+3,len(line)])]

        if prima[-1].isdigit():
            nearNumbers.append(prima.replace("*",".").replace(".",""))
        if dopo[0].isdigit():
            nearNumbers.append(dopo.replace("*",".").replace(".",""))
        #Line above and below
        aboveSub,belowSub = "",""

        #Above
        if i != 0:    
            fix=0
            if lines[i-1][leftIndex].replace("*",".") ==".":
                fix = 1

            aboveSub= lines[i-1][max([leftIndex-1,0]):rightIndex-1]
            
            sidesx = "."+lines[i-1][max([0,leftIndex-3]):leftIndex]
            sidedx = lines[i-1][leftIndex +fix :min([len(line), leftIndex+fix+4])]+"."
            #print("side:",sidesx,sidedx)
            b = lines[i-1][max([0,leftIndex-3]):min([leftIndex+4+fix,len(lines[i-1])])]
            if lines[i-1][leftIndex].replace("*",".")==".":
                if sidesx[-1].isdigit():
                    nearNumbers.append(sidesx.replace("*",".").replace(".","")) 
                if sidedx[0].isdigit():
                    nearNumbers.append(sidedx.replace("*",".").replace(".","")) 
            else:
                aboveNum = re.sub(r'\D','',b[sidesx.rfind("."): leftIndex+fix+ sidedx.find(".")]).replace("*",".").replace(".","")
                nearNumbers.append(aboveNum)
        #Below
        if i+1 < len(lines):
            fix=0
            if lines[i+1][leftIndex].replace("*",".")==".":
                fix = 1
            belowSub = lines[i+1][max([leftIndex-1,0]):rightIndex-1]

            sidesx = "."+lines[i+1][max([0,leftIndex-3]):leftIndex]
            sidedx = lines[i+1][leftIndex +fix :min([len(line), leftIndex+fix+4])]+"."
        
            b = lines[i+1][max([0,leftIndex-3]):min([leftIndex+4+fix,len(lines[i+1])])]
            if lines[i+1][leftIndex].replace("*",".")==".":
                if sidesx[-1].isdigit():
                    nearNumbers.append(sidesx.replace("*",".").replace(".","")) 
                if sidedx[0].isdigit():
                    nearNumbers.append(sidedx.replace("*",".").replace(".",""))             
            else:
                belowNum = b[sidesx.rfind("."): leftIndex+fix+ sidedx.find(".")].replace("*",".").replace(".","")
                nearNumbers.append(belowNum)
        #print(aboveNum,belowNum)
        
        print(nearNumbers)
        if len(nearNumbers) ==2:
            sum += int(nearNumbers[0])*int(nearNumbers[1])

        startSub= rightIndex - 1
        
print(sum)