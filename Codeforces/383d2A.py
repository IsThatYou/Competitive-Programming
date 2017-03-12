def fastexp(x,n,m):
    result = 1
    currentpower = x
    while n > 0:
        if n % 2 == 1:
            result = (result * currentpower) % m

        currentpower = (currentpower * currentpower) % m
        n = n//2

    return result

a = int(input())
b=fastexp(8, a, 10)
print(b)