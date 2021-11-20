import sys
input = sys.stdin.readline
# 이걸로 일단 선언 해두기
temp = input().split()

a = int(temp[0])-int(temp[1])
v = int(temp[2])-int(temp[1])
if (v % a) == 0:
    print(v//a)
elif (v % a) > 0:
    print(v//a+1)
