from functools import lru_cache

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

'''
Dynamic Programming using memoization
'''
fibonacci_cache = {}

def fibonacci_memo(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    if n == 0:
        value = 0
    elif n == 1:
        value = 1
    else:
        value = (fibonacci_memo(n-1) + fibonacci_memo(n-2))

    fibonacci_cache[n] = value
    return value


'''
Implement this problem using Python tools as LRU (Least Recently Used) 
cache, which provides a decorator
'''


@lru_cache(maxsize = 1000)
def fibonacci_lru(n):
    if type(n) != int:
        raise TypeError("n must be an integer number")
    #if n < 1:
    #    raise ValueError("n has to be positive")

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_lru(n-1) + fibonacci_lru(n-2)

if __name__ == "__main__":
    #fibonacci()
    '''
    for i in range(0, 20):
        print(getNthFib(i))

    for n in range(0, 50):
        print("Fib(",n,")",fibonacci_memo(n))
    '''
    print("Using LRU")
    for i in range(1, 51):
        print("Fib(",i,")",fibonacci_lru(i))

    print("Golden ratio")
    for i in range(1, 51):
        print("Golden(",i,")",fibonacci_lru(i+1) / fibonacci_lru(i))
    