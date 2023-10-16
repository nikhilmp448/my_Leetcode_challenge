x = "babad"
count = 0
for i in range(1,len(x)):
    if x[:i+1] == x[i::-1]:
        count +=1
        print(x[:i+1],x[i::-1])
print(count)

print(x[:2],x[2:4])