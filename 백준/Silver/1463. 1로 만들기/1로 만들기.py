N = int(input())

calList = [N]
count = 0

while N != 1:
    count += 1
    newCalList = []
    for num in calList:
        if num % 3 == 0:
            newCalList.append(num/3)
        if num % 2 == 0:
            newCalList.append(num/2)
        newCalList.append(num-1)
    if 1 in newCalList:
        break
    calList = newCalList

print(count)