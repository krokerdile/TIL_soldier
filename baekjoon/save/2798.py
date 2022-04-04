temp = input().split()
N = int(temp[0])
M = int(temp[1])

temp = input().split()
dep = []
for i in temp:
    dep.append(int(i))

max = 0
for i in range(N):
    for j in range(2,N):
        for k in range(3,N):
            if i==j or j==k or k==i:
                continue;
            # print(i,j,k)
            res = dep[i]+dep[j]+dep[k]
            if max<dep[i]+dep[j]+dep[k] and res <= M:
                max = res
print(max)
