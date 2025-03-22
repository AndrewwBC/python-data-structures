x = 1
for number in range(1,6):
    x = x * number
    print(x)

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(5))

def countTo0(number):
    print(number)
    if number == 0:
        return number
    else:
        return countTo0(number - 1)

print(countTo0(100))