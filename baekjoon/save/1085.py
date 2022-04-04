d = input().split()

x = int(d[0])
y = int(d[1])
w = int(d[2])
h = int(d[3])

t = [abs(w-x),abs(0-x),abs(h-y),abs(0-y)]
print(min(t))
