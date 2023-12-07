import re
lines = []

#with open("test.txt",'r') as f:
with open("input.txt",'r') as f:
    lines = f.readlines()

sum = 0

for i in range(len(lines)):
    lines[i] = re.sub(r'[^0-9.*]','.', lines[i])
    line = lines[i]

    numeri = re.findall("[*]",line)
    
    startSub = 0 #start substring position
    for num in numeri:
        nearNumbers = []

        leftIndex = startSub+ line[startSub:].index(num) #Index *
        
        #Left
        prima = line[max([leftIndex-3,0]):leftIndex] 
        #Right
        dopo = 0 
        rightIndex = leftIndex+len(num)
        if rightIndex != len(line):
            rightIndex = rightIndex+1
        
        dopo = line[rightIndex-1:min([rightIndex+3,len(line)])]

        if prima[-1].isdigit():
            nearNumbers.append(prima[prima.rfind(".")+1:])
        if dopo[0].isdigit():
            nearNumbers.append(dopo[:dopo.find(".")])

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

            b = lines[i-1][max([0,leftIndex-3]):min([leftIndex+4+fix,len(lines[i-1])])]
            
            if lines[i-1][leftIndex].replace("*",".")==".":
                if sidesx[-1].isdigit():
                    nearNumbers.append(sidesx[sidesx.rfind(".")+1:]) 
                if sidedx[0].isdigit():
                    nearNumbers.append(sidedx[:sidedx.index(".")])  
            else:             
                aboveNum = re.sub(r'\D','',b[sidesx.rfind("."):len(sidesx)-1+sidedx.find(".")])
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
                    nearNumbers.append(sidesx[sidesx.rfind(".")+1:]) 
                if sidedx[0].isdigit():
                    nearNumbers.append(sidedx[:sidedx.index(".")])            
            else:
                belowNum = re.sub(r'\D','',b[sidesx.rfind("."):len(sidesx)+sidedx.find(".")])
                nearNumbers.append(belowNum)
                
        if len(nearNumbers) ==2:
            print(nearNumbers,end="")
            sum += int(nearNumbers[0])*int(nearNumbers[1])
        startSub= rightIndex - 1
    
print(sum)