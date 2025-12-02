result1=0
result2=0
with open('C:/Users/pleas/Documents/AOC25/in2.txt','r') as file:
    while line := file.readline():
        my_list = line.split(",")
        for my_range in my_list:
            #print(my_range)
            for i in range(int(my_range.split("-")[0]),int(my_range.split("-")[1])+1):
                my_id=str(i)
                #part1
                first_half=my_id[:len(my_id)//2]
                if first_half+first_half==my_id:
                    #print(i)
                    result1+=i
                #part2
                for j in range(1,len(my_id)//2+1):
                    my_part=''
                    for k in range(0,len(my_id)//len(my_id[0:j])):
                        my_part=my_part+my_id[0:j]
                    #print(my_part,my_id)
                    if my_part==my_id:
                        result2+=i
                        #print('match')
                        break
print(result1,result2)