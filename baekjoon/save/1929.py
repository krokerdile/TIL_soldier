data = input().split()

sp = int(data[0])
ep = int(data[1])

ans = []
for i in range(2,ep+1):
    ans.append(i)

for i in ans:
        # for j in range(2, int(i**0.5) + 1):
        #     if j % i == 0:
        #         ans.remove(j)
    count = 1
  #  print("count : %d" % i////)/
    while 1: 
        count += 1
        if i*count in ans:
            #print(i*count)
            ans.remove(i*count)
        if i*count > ep:
            break;
        
    # if i==2:
    #     ans.append(i)
        
    # elif i==3:
    #     ans.append(i)
    # else:
    #     cp = 0
    #     for j in ans:
    #         if i%j == 0:
    #             cp = -1
    #     if cp!=-1:
    #         ans.append(i)
    
        
for i in ans:
    if i>=sp:
        print(i)