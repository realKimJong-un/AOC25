result1=0
result2=0
with open('C:/Users/pleas/Documents/AOC25/in3.txt','r') as file:
    while line := file.readline().strip("\n"):
        for i in range(0,len(line)):
            if line[i]==max(line[:-1]):
                #print(line,max(line[:-2]),i, line[i])
                result1+=int(f"{line[i]}{max(line[i+1:])}")
                break
        #part 2
        digits=''
        lower_limit=0
        upper_limit=-11
        for i in range(0,len(line)):
            #print(digits,lower_limit,upper_limit)
            if upper_limit==0:upper_limit=len(line)
            if line[i]==max(line[lower_limit:upper_limit]):
                digits+=line[i]
                lower_limit=i+1
                upper_limit+=1
            if len(digits)==12:
                result2+=int(digits)
                break
print(result1,result2)
