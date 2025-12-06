result1=0
result2=0
sheet=[]
with open('C:/Users/pleas/Documents/AOC25/in6.txt','r') as file:
    while line := file.readline().strip():
        sheet.append(line.split())
for ids, sign in enumerate(sheet[-1]):
    multi=1
    if sign == '+':
        for line in sheet[:-1]:
            result1+=int(line[ids])
    elif sign == '*':
        for line in sheet[:-1]:
            multi*=int(line[ids])
        result1+=multi
    else:print('error')
#part2
signs=sheet[-1]
sheet=[]
with open('C:/Users/pleas/Documents/AOC25/in6.txt','r') as file:
    while line := file.readline().strip('\n'):
        sheet.append([line[i:i+1] for i in range(0, len(line), 1)])
sheet=sheet[:-1]
#
sheet=list(map(list, zip(*sheet)))
print(sheet)
#for ids, sign in enumerate(signs):
sheet.append([''])

temp=[]
i=0
for number in sheet:
    if ''.join(number).strip()=='':
        #print(temp,signs[i])
        if signs[i] == '+':
            add=0
            for t in temp:
                add+=t
            #print(add)
            result2+=add
        if signs[i] == '*':
            multi=1
            for t in temp:
                multi*=t
            print(multi)
            result2+=multi
        i+=1
        temp=[]
    else:
        temp.append(int(''.join(number).strip()))
print(result1,result2)
