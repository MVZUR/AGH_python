def fibonacci_gen(n):
    a=0
    b=1
    for i in range(n-1):
        c = a + b
        a = b
        b = c
        yield c

n = 10
output = fibonacci_gen(n)
for number in output:
    print(number)