result1=0
result2=0
with open("in7.txt") as file:
    while line := list(file.readline().strip('\n')):
        #print(line)
        if not 'S' in line:
            #print('kein S')
            for i, digit in enumerate(line):
                if last_line[i]=='S': line[i]=1
                elif isinstance(last_line[i], int):
                    #print('beam')
                    if line[i]=='.':line[i]=last_line[i]
                    elif isinstance(line[i], int):line[i]+=last_line[i]
                    elif line[i] == '^':
                        if isinstance(line[i-1], int):line[i-1]+=last_line[i]
                        elif line[i-1]=='.':line[i-1]=last_line[i]
                        line[i+1]=last_line[i]
                        result1+=1
                        #print('boom')
        last_line=line
        #print(line)
for digit in last_line:
    if isinstance(digit, int):
        result2+=digit
print(result1, result2)
