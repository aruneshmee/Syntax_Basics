def divisibleSumPairs(n, k, ar):
    count=0
    for _ in range(0, len(ar)):
        x = ar[0]
        for y in ar[1:]:
            if (x + y)%k==0:
                count+=1
        ar.pop(0)
    return count

# Ordered Dictionary
from collections import OrderedDict
count = OrderedDict()
for i in ar:
    count.setdefault(i, 0)
    count[i] += 1
    
x = max(count, key=count.get)
print( x)

#Array Manu
def miniMaxSum(arr):
    mins=0
    maxs=0
    arr.sort()
    a = arr.pop(0)
    for i in arr:
        maxs += i
    arr.pop(-1)
    arr.append(a)
    arr.sort()
    for i in arr:
        mins += i
    print(mins,maxs)

# dictionaries and maps
n = int(input())
book ={}
for _ in range(n):
    item = input().split()
    book[item[0]]=int(item[1])

while True:
    try:
        query = input()
    except EOFError:
        break
    if query in book:
        print(query,'=',book[query])
    else:
        print('Not found')
