def fun(num):
    i=0
    sum=0
    while i<len(num):
        sum=sum+num[i]
        i+=1
    print(sum)
fun([8,2,3,0,7])