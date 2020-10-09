# here our programming basics starts

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

# the sum of two elements defines the next: Fibonacci series

i = 256*256
print('The value of i is', i)

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b

