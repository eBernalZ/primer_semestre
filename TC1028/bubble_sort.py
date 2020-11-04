list = [5,1,4,2,8]
for j in range(len(list)-1):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            temp = list[i+1]
            list[i+1] = list[i]
            list[i] = temp
print(list)
