dial=50
result=0
with open('C:/Users/pleas/Documents/AOC25/in1.txt','r') as file:
    while line := file.readline():
        if line[0]=='L':
            dial-=int(line[1:])
        elif line[0]=='R':
            dial+=int(line[1:])
        if dial%100==0:result+=1
print(result)

dial=50
result2=0
with open('C:/Users/pleas/Documents/AOC25/in1.txt','r') as file:
    while line := file.readline():
        for i in range(int(line[1:])):
            if line[0]=='L':dial-=1
            elif line[0]=='R':dial+=1
            if dial%100==0:result2+=1
print(result2)