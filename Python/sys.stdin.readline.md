input()을 사용하지 않고 대부분의 백준 문제 파이썬 풀이에서 sys.stdin.readline를 사용하는 이유?
-> input()으로 계속해서 입력을 받으면 시간초과가 나올 수 있음
(시간초과가 나는 이유는 뭘까?)

한 개의 정수를 입력받을 때
    import sys
    a = int(sys.stdin.readline())