'''
FizzBuzz is just a game in which the program has to return:
    If a number is divisible by 3 returns the string "Fizz"
    If the number is divible by 5 returns the string "Buzz"
    If it's divisible by 3 and 5 returns this string "FizzBuzz"
'''

def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizzbuzz()
