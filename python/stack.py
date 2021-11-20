import sys
number = input()
input = sys.stdin.readline().split()

temp = []
for i in range(int(number)):
    line = input()
    if "push" in line:
        temp.append(line[1])
    elif "top" in line:
        if len(temp) == 0:
            print(-1)
        else:
            print(temp[len(temp)-1])
    elif "size" in line:
        print(len(temp))
    elif "empty" in line:
        if len(temp) == 0:
            print(1)
        else:
            print(0)
    elif "pop" in line:
        if(len(temp) != 0):
            print(temp.pop())
        else:
            print(-1)
