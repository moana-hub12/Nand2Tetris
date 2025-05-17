def parse(todecode):
    index=0
    splitcount=0
    for k in todecode:
        for i in k:
            if( "=" in k) and (";" in k):
                splitted=k.split('=')
                split2=splitted[1].split(';')
                splitcount=2
            elif i=='@' or i== '=' or i==';':
                splitted = k.split(i)
                if i== '=':
                    splitted.append('')
                elif i==';':
                    splitted.reverse()
                    splitted.append('')
                    splitted.reverse()
                splitcount=1
        if splitcount<=1:
            todecode[index]=splitted
        else:
            splitted[1]=split2[0]
            splitted.append(split2[1])
            todecode[index]=splitted
        index+=1
    for i in todecode:
        if len(i)==3:
            temp=i[1]
            i[1]=i[0]
            i[0]=temp
    return todecode