result1 = 0
result2 = 0
instructs=[]

def update_out():
    truf=False
    for instruct in instructs:
        #if -1 == instruct[2][0]:
        if 'out' in instruct[1]:
            instruct[2][0]=1
            instruct[2][1:4]=[0,0,0]
            truf=True
        else:
            outi=[]
            for insti in instructs:
                if insti[0] in instruct[1]:
                    outi.append(insti[2])
                if outi and all(-1 not in sub for sub in outi):
                    instruct[2] = [sum(sub[i] for sub in outi) for i in range(4)]
                    truf=True
        if 'dac' == instruct[0] and -1!=instruct[2][0]:
            instruct[2][1]=instruct[2][0]
            truf=True
        elif 'fft' == instruct[0]:
            instruct[2][2]=instruct[2][0]
            truf=True
        if 'fft' == instruct[0]:
            instruct[2][3]=instruct[2][1]
            truf=True
        if 'dac' == instruct[0]:
            instruct[2][3]=instruct[2][2]
        if 'svr' == instruct[0]:
            print('sol:',instruct[2][3])
            result2=instruct[2][3]
            if result2!=0:
                truf=False
    return truf

with open("in11.txt") as file:
    while line := file.readline().strip('\n'):
        #reading
        #aaa: you hhh
        name=line[:3]
        exits=line[5:].split(' ')
        #out	dac+out		fft+out		dac+fft+out
        instructs.append([name,exits,[-1,-1,-1,-1]])
#print(instructs[0])

i=0
while update_out():
    i+=1
    if i%100000==0:print('piep')

for line in instructs: print(line)
print(result2)