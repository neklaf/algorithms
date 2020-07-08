'''
Fibonacci sequence is defined as follows: the first number of the sequence is 0,
the second number of the sequence is 1, and the nth number is the sum of the 
(n-1)th and the (n-2)th numbers:
   0, 1, 1, ..., Fib(n-1) + Fib(n-2)
'''

'''
Method returning a the Fibonacci sequence to the 10th element
'''
def fibonacci():
    a, b = 0, 1
    for i in range(0, 10):
        print("Fib(",i,"): ",a)
        a, b = b, a + b

'''
Recursive implementation
   Cuadratic execution time O(n^2)
'''
def getNthFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (getNthFib(n-1) + getNthFib(n-2))

if __name__ == "__main__":
    fibonacci()

    print(getNthFib(7))

'''
Dynamic Programming solution
'''
