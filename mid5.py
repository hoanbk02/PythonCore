import math
n = int(input("Nhập n: "))
square = int(math.sqrt(n))
count = 0
for num in range(2,n):
    for i in range(2, square + 1):
        if num%i==0:
            break
        else: 
            count += 1
print(count)