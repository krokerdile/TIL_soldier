data = input().split()

sp = int(data[0])
ep = int(data[1])
# n=100

def isPrime(a):
    if(a<2):
        return False
    for i in range(2,a):
        if(a%i==0):
            return False
    return True

for i in range(ep+1):
    if(isPrime(i)) and sp<=i and ep>=i:
        print(i)