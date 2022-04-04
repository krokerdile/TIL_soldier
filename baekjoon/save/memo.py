import sys
import operator
# input = sys.stdin.readline

def dec_find(t):
    temp = []
    n = t
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
    return li

while 1 :
    ini = 3
    n = int(input())
    temp = []
    temp = dec_find(n)
    if n == 0:
        break
    end_key = -1
    while end_key!=0:
        if (n-ini)%2 !=0:
            print('{num1} = {num2} + {num3}'.format(num1=n, num2 = ini, num3 = n-ini))
            break
        if ini > n:
            print("Goldbach's conjecture is wrong.")
            break


        