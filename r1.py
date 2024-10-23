def fuct(x):
    if x ==1:
        return 1
    return fuct(x-1)*x
# print(fuct(5))

def fib(x):
    if x ==1:
        return 0
    elif x ==2:
        return 1
    return fib(x-1) + fib(x-2)

# print(fib(8))

def power(n,x):
    if x == 0:
        return 1
    if x < 0:
        return 1/power(n,-x)
    if not x%2:
       return power(n,x//2)*power(n,x//2)
    else:
        return power(n,x-1)*n

print(power(2,-1))