a = int(input())
count = 0
while 1 :
    if a%5>=0:
        if a%5!=0 and a%5!=3 :
            # print(a)
            pass
        else:
            count += a/5
            # print(count)
            a=a%5
            # print(a)
            if a==0:
                print(int(count))
                break
    if a%3>=0:
        # print(a)
        count += a/3
        # print(count)
        a=a%3
        # print(a)
        if a==0:
                print(int(count))
                break    
    if a>0 and a<3:
        print(-1)
        break