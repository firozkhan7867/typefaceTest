first = input("Enter 1st String : ")


sec =input("Enter 2nd String : ")

count = 0
for i in first:
    if i == sec[-1]:
        count +=1

print(count)


