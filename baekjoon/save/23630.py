from itertools import combinations

a = int(input())

data = list(map(int, input().split()))
# lstn = list(map(int, input().split()))
# print(list(combinations(data, 5)))
for i in reversed(range(a+1)):
    print(combinations(data,i))
    
temp = 1
for i in data:
    
    
    