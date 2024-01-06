# I wanted to test if Python random follows the normal distribution bell curve

import random

numbers = []
count = 0
sum = 0

while(1):
    count = count + 1
    r = random.randint(0,10000)
    numbers.append(r)
    sum = sum + r
    if r == 9999:
        break

numbers.sort()
print(numbers)

# median
divBy = count / 2
index = round(divBy)
    
print("median ")
print(numbers[index])
    
avg = sum / count
print("avg " + str(avg))