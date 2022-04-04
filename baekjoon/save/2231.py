N = input()
N = int(N)
Min = 1000001
for i in range(0,N):
    temp = N-i #임시로 저장해놓고
    str_num = str(temp)
    # print(str_num)
    str_num = list(str_num)
    # print(str_num)
    sum_num = 0
    for j in str_num:
        sum_num += int(j)
    if temp+sum_num == N:
        if temp<Min : Min = temp
if Min != 1000001:
    print(Min)
else:
    print(0)