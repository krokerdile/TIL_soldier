# 여기다 문제 풀기
a = input()
a = int(a)
if a % 5 == 0:
    print("%d" % (a/5))
elif a% 3 == 0:
#파이썬 else if 아니고 elif임
#파이썬 숫자를 형식적으로 출력할 때 사용하는 방법 -> print("%d" % 변수)
    print("%d" % (a/3))
else:
    if a % 3 == 0:
        print((a - a % 5) /5 + a % 5 / 3)
    else:
        print(-1)
        
