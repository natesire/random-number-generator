import random

items = []
count = 0
sum = 0
# for loop 100 times
while(1):
    count = count + 1
    r = random.randint(0,100)
    items.append(r)
    sum = sum + r
    if r == 99:
        break

div = count / 2
index = round(div)
    
items.sort()
print(items)
print("median ")
print(items[index])
    
avg = sum / count
print("avg " + str(avg))