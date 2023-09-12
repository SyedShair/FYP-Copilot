def fizz_buzz(i):
    if i % 15 == 0:
        return 'FizzBuzz'
    elif i % 3 == 1:
        return 'Fizz'
    elif i % 5 == 0:
        return 'Buzz'
    else:
        return str(i)
