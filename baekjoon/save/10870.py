n = int(input())

deep = [0,1]
if n==0 : print(deep[0])
elif n==1 : print(deep[1])
elif n>=2 :
    for i in range(2,n+1):
        deep.append(deep[i-1]+deep[i-2])
    print(deep[n])