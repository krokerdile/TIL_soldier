t = int(input()) #테스트 케이스 개수

for test in range(t):
    k = int(input()) #몇 층까지
    n = int(input()) #몇 호실 까지


    temp = []

    for i in range(1,n+1):
        temp.append(i)

    for i in range(k):
        for j in range(n-1):
            temp[j+1] += temp[j]

    print(temp[n-1])