import pandas

country=input()
#job=input()

data=[]
row=[]
result=[]

with open("data.txt", "r") as f:
    next(f)
    sum=0
    for line in f:
        row=line.rstrip().split(",")
        #if row[4]==country and row[7]==job:
        if row[4]==country:
            #result.append(int(row[3]))
            if ".org" in line: #if "https://" in line:
                sum+=1
print(sum)
    #print(sum(result))
