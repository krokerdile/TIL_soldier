import sys
input = sys.stdin.readline
# 이걸로 일단 선언 해두기
n = input().split()
n1 = int(n[0])
n2 = int(n[1])
count = 0
for i in range(n1,n2+1):
    ans = int(i)
    for i in range(1,ans):
        if i!=1 and ans%i==0:
            ans = -1
            break
    if ans == 1:
        ans = -1
    if ans == -1:
        continue
    else: 
        print(ans)