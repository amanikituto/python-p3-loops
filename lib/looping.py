# looping.py

def happy_new_year():
    """Counts down from 10 to 1, then prints 'Happy New Year!'"""
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")

def square_integers(numbers):
    """Squares each integer in a list and returns the squared list."""
    return [num**2 for num in numbers]

def fizzbuzz():
    """Prints numbers 1 to 100, replacing multiples of 3, 5, or both."""
    for num in range(1, 101):
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
