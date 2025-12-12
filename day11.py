result1 = 0
result2 = 0
instructs=[]
todo=[[1,'you']]

def update(val,name):
    if name=='out':
        return val
    for i in range(len(instructs)):
        if instructs[i][1]==name:
            for exi in instructs[i][2]:
                todo.append([val,exi])
            break
    return 0

with open("in11.txt") as file:
    while line := file.readline().strip('\n'):
        #reading
        #aaa: you hhh
        name=line[:3]
        exits=line[4:].split(' ')
        instructs.append([0,name,exits])

while todo:
    #print(len(todo))
    temp=todo.pop()
    result1+=update(temp[0],temp[1])
    


print(result1, result2)