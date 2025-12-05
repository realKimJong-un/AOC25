result1=0
result2=0
my_ranges=[]
with open('C:/Users/pleas/Documents/AOC25/in5.txt','r') as file:
    while line := file.readline():
        if '-' in line:
            my_range=line.split('-')
            my_ranges.append([int(my_range[0]),int(my_range[1])])
        elif line!='\n':
            for ran in my_ranges:
                if  ran[0] <= int(line) <= ran[1]:
                    result1+=1
                    break
#part2
deleted=0
for i in range (len(my_ranges)):
    #print (my_ranges[i-deleted])
    for j in range (len(my_ranges)):
        if i-deleted==j:continue
        #print (my_ranges[j])
        if my_ranges[j][0] <= my_ranges[i-deleted][0] <= my_ranges[j][1]:
            if my_ranges[j][0] <= my_ranges[i-deleted][1] <= my_ranges[j][1]:#subset
                del my_ranges[i-deleted]
                deleted+=1
                break
            elif my_ranges[j][1] <= my_ranges[i-deleted][1]:#overlap
                my_ranges[j][1] = my_ranges[i-deleted][1]
                del my_ranges[i-deleted]
                deleted+=1
                break
        if my_ranges[j][0] <= my_ranges[i-deleted][1] <= my_ranges[j][1]:#overlap
                my_ranges[j][0] = my_ranges[i-deleted][0]
                del my_ranges[i-deleted]
                deleted+=1
                break
        #print (my_ranges)
for ran in my_ranges:
    result2+=ran[1]-ran[0]+1
print(result1,result2)
