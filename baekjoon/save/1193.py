n = int(input()) #몇 번째 분수인지   
count = 1
max_n = 1
max_b = 0 
while 1:
    # print(n,max_n)
    if n <= max_n:
        # print(max_n)
        k = count+1
        n = n-max_b
        # print(k,n)
        # print(count)
        break
        
    count += 1
    max_b = max_n
    max_n += count
    
    # print(max_n)


check = 0
if k%2 == 0:
    for i in range(1,k):
        check += 1
        # print(check)
        if check == n:
            print("%d/%d" %(k-i,i)) 
if k%2 != 0:
    for i in range(1,k):
        check += 1
        # print(check)
        if check == n:
            print("%d/%d" %(i,k-i))      
    

            


    