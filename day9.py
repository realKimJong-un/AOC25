import numpy as np
from numpy.linalg import norm
from collections import deque

result1=0
result2=0
boxes=[]
possible_connections=[]    

with open("in9.txt") as file:
    while line := file.readline().strip('\n'):
        temp=[]
        for coord in line.split(','):
            temp.append(int(coord))
        boxes.append(temp)

for i1 in range (len(boxes)):
    for i2 in range (i1+1,len(boxes)):
        dis_vec = np.array(boxes[i1]) - np.array(boxes[i2])
        dis=(abs(dis_vec[0])+1)*(abs(dis_vec[1])+1)
        possible_connections.append([dis,i1,i2])
possible_connections=sorted(possible_connections, reverse=True)

result1=possible_connections[0][0]
print(f'result p1: {result1}')

edges = []
n = len(boxes)
for i in range(n):
    (x1,y1) = boxes[i]
    (x2,y2) = boxes[(i+1) % n]

    if x1 == x2:   # vertikale Kante
        edges.append((x1, min(y1,y2), max(y1,y2)))


new_filled=[]

ys = [y for _,y in boxes]
min_y, max_y = min(ys), max(ys)

for y in range(min_y, max_y+1):
    
    intersections = []
    for (x, y1, y2) in edges:
        if y1 <= y <= y2:   # richtige Scanline-Regel
            intersections.append(x)

    intersections.sort()
    intervals = []
    
    if len(intersections)==3:
        intersections.pop(1)
    elif len(intersections)==5:
        intersections.pop(1)
        intersections.pop(1)
        intersections.pop(1)
    if len(intersections)%2==0:    
        for i in range(0, len(intersections), 2):
            intervals.append([intersections[i], intersections[i+1]])
    new_filled.append([y, intervals])
    

def point_in_polygon(x, y):
    for sy, intervals in new_filled:
        if sy == y:
            for x_start, x_end in intervals:
                if x_start <= x <= x_end:
                    return True
            return False
    return False 

def rect_inside(x1, y1, x2, y2):
    # stelle sicher: x1 <= x2, y1 <= y2
    if x2 < x1: x1, x2 = x2, x1
    if y2 < y1: y1, y2 = y2, y1

    for sy, intervals in new_filled:
        if sy < y1 or sy > y2:
            continue

        # Prüfen ob in dieser Zeile ein Intervall das Rechteck komplett abdeckt
        covered = False
        for xs, xe in intervals:
            if xs <= x1 and xe >= x2:
                covered = True
                break

        if not covered:
            return False  # eine Zeile war nicht vollständig abgedeckt → Rechteck liegt nicht drin

    return True  # jede Zeile ist vollständig abgedeckt

for num, square in enumerate(possible_connections):
    if num % 10000 == 0:print(num,len(possible_connections))

    i, j = square[1], square[2]
    x1, y1 = boxes[i]
    x2, y2 = boxes[j]

    if rect_inside(x1, y1, x2, y2):
        result2 = square[0]   # Fläche
        break

print(result1, result2)