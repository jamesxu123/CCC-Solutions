def fib(n):
        count = 0
        if n == 1 or n == 2:
                return 1
        else:
                return fib(n-1)+fib(n-2)
print(fib(int(input())))
