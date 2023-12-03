import re
#12 red, 13 green, 14 blue
COLORS = {"red":12 , "green":13 , "blue":14}

with open('input.txt','r') as f:
    lines = f.readlines()

def first():
    somma = 0
    for line in lines:
        flag = True
        for l in line.split(";"):
            subSplit = [str.strip(i).replace(",","") for i in l.split(" ")][1:]
            for c,v in COLORS.items(): 
                if subSplit.count(c) >0:
                    index = subSplit.index(c)-1
                    if index >= 0:
                        if int(subSplit[index]) > v:
                            flag=False

        if flag:
            somma += int(line[line.find(" "):line.find(":")].strip())

    print(somma)

def second():
    sop = 0 #Som of product
    for line in lines:
        element = []
        for l in line.split(";"):
            subSplit = [str.strip(i).replace(",","") for i in l.split(" ")][1:]
            for c,v in COLORS.items(): 
                if subSplit.count(c) >0:
                    index = subSplit.index(c)-1
                    if index >= 0:
                        element.append(int(subSplit[index]))
                else:
                    element.append(0)
        sop += max(element[::3])*max(element[1::3])*max(element[2::3])
    print(sop)

first()
second()