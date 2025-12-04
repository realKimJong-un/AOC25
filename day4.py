result1=0
result2=0
diagram=[]
with open('C:/Users/pleas/Documents/AOC25/in4.txt','r') as file:
    while line := file.readline().strip("\n"):
        if not diagram: diagram.append(['.'] * (len(line)+2))
        diagram.append(list(f".{line}."))
    diagram.append(diagram[0])
for i in range(1,len(diagram)):
    for j in range(1,len(diagram[i])):
        if diagram[i][j] == '@':
            rolls=0
            for x in range(-1,2):
                for y in range(-1,2):
                    #print(x,y)
                    if diagram[i+y][j+x]=='@':rolls+=1
            if rolls<5:
                #diagram[i][j] == 'x'
                result1+=1
#part2
delta=1
while delta:
    delta=0
    #for line in diagram:print(line)
    for i in range(1,len(diagram)):
        for j in range(1,len(diagram[i])):
            if diagram[i][j] == '@':
                rolls=0
                for x in range(-1,2):
                    for y in range(-1,2):
                        #print(x,y)
                        if diagram[i+y][j+x]=='@':rolls+=1
                if rolls<5:
                    diagram[i][j] = 'x'
                    delta+=1
    result2+=delta       
print(result1,result2)
