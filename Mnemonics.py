def ainst(value):
    valuei = int(value)
    valuer='0000000000000000'
    div=1
    i=0
    bin=0
    while div!=0:  
        div = valuei//2
        rem = valuei%2
        valuei=div
        bin+=rem*(10**i)
        i+=1
    binary = str(bin)
    lent= 16-len(binary)
    valueb = valuer[0:lent] + binary
    return valueb

def ccomp(comp):
    compdict = {'0':'101010', '1':'111111', '-1':'111010', 'D':'001100', 'A':'110000', 'M':'110000', '!D':'001101', '!A':'110001', '!M':'110001', '-D':'001111', '-A':'110011', '-M':'110011', 'D+1':'011111', 'A+1':'110111', 'M+1':'110111', 'D-1':'001110', 'A-1':'110010', 'M-1':'110010', 'D+A':'000010', 'D+M':'000010', 'D-A':'010011', 'D-M':'010011', 'A-D':'000111', 'M-D':'000111', 'D&A':'000000', 'D&M':'000000', 'D|A':'010101', 'D|M':'010101'}
    if 'M' in comp:
        compb = '1'+ compdict[comp]
    else:
        compb = '0'+ compdict[comp]
    return compb
    
def cdest(dest):
    destdict = {'':'000','M':'001','D':'010','MD':'011','A':'100','AM':'101','AD':'110','AMD':'111'}
    destb = destdict[dest]
    return destb

def cjump(jump):
    destjump = {'':'000','JGT':'001','JEQ':'010','JGE':'011','JLT':'100','JNE':'101','JLE':'110','JMP':'111'}
    jumpb = destjump[jump]
    return jumpb