for num in range(1,500):
    sum=0
    if num>1:
        for i in range(1,num):
            if num%i==0:
                sum+=i

        if sum==num:
            print(num)