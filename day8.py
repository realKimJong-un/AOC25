import numpy as np
from numpy.linalg import norm


result1=0
result2=0
boxes=[]
possible_connections=[]
connections=[]
circs=[]
with open("in8.txt") as file:
    while line := file.readline().strip('\n'):
        temp=[]
        for coord in line.split(','):
            temp.append(int(coord))
        boxes.append(temp)
#print(boxes)
print('check all possible connections')
#for i1,box1 in enumerate(boxes):
for i1 in range (len(boxes)):
    print(f'{i1}/{len(boxes)}')
    #for i2,box2 in enumerate(boxes):
    for i2 in range (i1+1,len(boxes)):
        #if i1==i2:continue
        connected=False
        #for possible_connection in possible_connections:
        #    if i1 in possible_connection and i2 in possible_connection:connected=True
        #if  connected:continue
        dis_vec = np.array(boxes[i1]) - np.array(boxes[i2])
        dis=dis_vec[0]*dis_vec[0]+dis_vec[1]*dis_vec[1]+dis_vec[2]*dis_vec[2]
        #dis = dis_vec[0]^2+dis_vec[1]^2+dis_vec[2]^2
        #dis = norm(np.array(box1) - np.array(box2))
        possible_connections.append([dis,i1,i2])
#print('sorting')
possible_connections.sort()#=sorted(possible_connections, key=lambda x: x[0])
#print('done')
for i in range(1000):
    connections.append([possible_connections[i][1],possible_connections[i][2]])
    one_in=-1
    two_in=-1
    for ic,circ in enumerate(circs):
        if possible_connections[i][1] in circ:one_in=ic
        if possible_connections[i][2] in circ:two_in=ic
    if one_in==two_in and one_in !=-1:continue
    elif one_in!=-1 and two_in!=-1:
        circs[one_in].extend(circs[two_in])
        circs.pop(two_in)
    elif one_in!=-1:circs[one_in].append(possible_connections[i][2])
    elif two_in!=-1:circs[two_in].append(possible_connections[i][1])
    else:circs.append([possible_connections[i][1],possible_connections[i][2]])
#print(connections)
#for connection in connections:print(boxes[connection[0]],boxes[connection[1]])
#print(circs)
result1=1
for circ in sorted(circs, key=len, reverse=True)[:3]:
    result1*=len(circ)

i=1000
while True:
    connections.append([possible_connections[i][1],possible_connections[i][2]])
    one_in=-1
    two_in=-1
    for ic,circ in enumerate(circs):
        if possible_connections[i][1] in circ:one_in=ic
        if possible_connections[i][2] in circ:two_in=ic
    if one_in==two_in and one_in !=-1:pass
    elif one_in!=-1 and two_in!=-1:
        circs[one_in].extend(circs[two_in])
        circs.pop(two_in)
    elif one_in!=-1:circs[one_in].append(possible_connections[i][2])
    elif two_in!=-1:circs[two_in].append(possible_connections[i][1])
    else:circs.append([possible_connections[i][1],possible_connections[i][2]])
    if len(circs[0])==len(boxes):
        result2=boxes[connections[-1][0]][0]*boxes[connections[-1][1]][0]
        break
    i+=1


print(result1, result2)


'''
for i in range(1000):
    short_dis=[]
    for i1,box1 in enumerate(boxes):
        for i2,box2 in enumerate(boxes):
            #same?
            if i1==i2:continue
            #in same circ
            #connected=False
            #for circ in circs:
            #    if i1 in circ and i2 in circ:connected=True
            #if  connected:continue
            #connected?
            connected=False
            for connection in connections:
                if i1 in connection and i2 in connection:connected=True
            if  connected:continue
            #distance
            dis = norm(np.array(box1) - np.array(box2))
            if not short_dis or dis<short_dis[0]:short_dis= [dis,i1,i2]
    connections.append([short_dis[1],short_dis[2]])
    #sort circs
    one_in=-1
    two_in=-1
    for ic,circ in enumerate(circs):
        if short_dis[1] in circ:one_in=ic
        if short_dis[2] in circ:two_in=ic
    if one_in!=-1 and two_in!=-1:
        circs[one_in].extend(circs[two_in])
        circs.pop(two_in)
    elif one_in!=-1:circs[one_in].append(short_dis[2])
    elif two_in!=-1:circs[two_in].append(short_dis[1])
    else:circs.append([short_dis[1],short_dis[2]])
#print(connections)
#for connection in connections:print(boxes[connection[0]],boxes[connection[1]])
#print(circs)
    result1=1
    for circ in sorted(circs, key=len, reverse=True)[:3]:
        result1*=len(circ)
print(result1, result2)
'''