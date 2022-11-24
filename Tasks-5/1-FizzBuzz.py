num = 7

def FizzBuzz(num):
    if(num < 0):
        print("Error. Negative number.")
    else:
        if(num % 3 == 0 and num % 5 == 0):
            print("Fizz Buzz")
            return
        if(num % 3 == 0):
            print("Fizz")
        if(num % 5 == 0):
            print("Buzz")
        if(num % 3 != 0 and num % 5 != 0):
            print(num)

FizzBuzz(num)