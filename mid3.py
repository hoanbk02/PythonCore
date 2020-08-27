x  = input()
count = {}
for i in x:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1
 
for i in sorted(count, key=count.get, reverse=False):
    print(i, count[i])