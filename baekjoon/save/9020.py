N = int(input())
t = []
for i in range(N):
    t.append(int(input()))
n = max(t)

temp = []

for i in range(2,n+1):
    temp.append(i)
for i in range(2,n+1):
    count = 0;
    while 1:
        count += 1
        if i*count > n:
            break;
        if temp[i*count-2]==-1:
            continue;
        if count == 1:
            continue;
        if temp[i*count-2]!=-1:
            temp[i*count-2]=-1
remove_set = {-1}

li = [i for i in temp if i not in remove_set]
for put in t:
    ans = []
    check = 0
    for i in li :
        if check == -1:
            break;
        if i>=put/2:
            if i*2 == put:
                ans = [i,i]
                break;
            else:
                for j in li:
                    if i+j == put:
                        check = -1
                        ans = [j,i]
                        break;
    print(ans[0],ans[1])
