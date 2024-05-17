"""
    FILL IN THE CODE

    such that it will print number for 1 to N
    BUT if the number is multiple of 3, print "Fizz" instead
    BUT if the number is multiple of 5, print "Buzz" instead
    BUT if it's multiple of 3 and 5, print "FizzBuzz" instead

    @param n
"""


def fizz_buzz(n: int):
    for i in range(1, n+1):
        print(i)
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")


    pass


if __name__ == "__main__":
    fizz_buzz(20)
