a = int(input())
count = 0
while 1 :
    if a%5==0:
        count += a/5
        a=a%5
    if a-3>=0:
        count += 1
        a = a-3
    if a==0:
        print(int(count))
        break;
    if a-3 < 0:
        print(-1)
        break;