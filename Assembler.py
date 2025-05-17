from parser import parse
from mnemonics import ainst,ccomp,cdest,cjump

filename = input("enter the file name : ")
todecode = []
with open (filename,'r') as f:
    for line in f:
        contents = line.strip()
        tempstr = ""
        for i in contents:
            if i=='/' or i=="" or i=="#":
                break
            elif i==" ":
                break
            else:
                tempstr+=i    
        todecode.append(tempstr)

index=0
while index<len(todecode):
    if todecode[index]=="":
        todecode.pop(index)
    else:
        index+=1


symbol_table = {"R0": 0,"R1": 1,"R2": 2,"R3": 3,"R4": 4,"R5": 5,"R6": 6,"R7": 7,"R8": 8,"R9": 9,"R10": 10,"R11": 11,"R12": 12,"R13": 13,"R14": 14,"R15": 15,"SCREEN": 16384,"KBD": 24576,"SP": 0,"LCL": 1,"ARG": 2,"THIS": 3,"THAT": 4}
n=16
def variable(name,index):
    global symbol_table, n
    if name in symbol_table.keys():
        pass 
    elif index!='':
        symbol_table[name]=index
    else:
        symbol_table[name]=n
        n+=1
    return str(symbol_table[name])

index=0
for i in todecode:
    if i[0]=='(':
        l=len(i)
        label = i[1:l-1]
        variable(label,index)
        index-=1
    index+=1

index=0
while index<len(todecode):
    if todecode[index][0]=="(":
        todecode.pop(index)
    else:
        index+=1

index=0
parsed=parse(todecode)
for i in parsed:
    if len(i)==2:
        if not(i[1].isdigit()):
            temp=variable(i[1],'')
            value=ainst(temp)
        else:
            value=ainst(i[1])
        parsed[index]=value
        index+=1
    if len(i)==3:
        comp=ccomp(i[0]) 
        dest=cdest(i[1])
        jump=cjump(i[2])
        cvalue='111'+comp+dest+jump
        parsed[index]=cvalue
        index+=1

filenameb = input("enter the file name you want to store the processed file : ")
with open (filenameb,'w',newline='\n') as f:
    lent = len(parsed)-1
    index=0
    for i in parsed:
        f.write(i)
        if index != lent:
            f.write('\n')
        index+=1