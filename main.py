def func1(n):
    return n*(n+1)/2

def func2(n):
    sum=0
    for i in range(1,1+n):
        sum+=i

    return sum

print (func1(6))
print (func2(6))
