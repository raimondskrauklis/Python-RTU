for fizzbuzz in range(1, 100):
    if fizzbuzz % 5 == 0:
        print("Fizz", end=",")
        continue
    elif fizzbuzz % 7 == 0:
        print("Buzz", end=",")
        continue
    elif fizzbuzz % 35 == 0:
        print("FizzBuzz", end=",")
        continue
    print(fizzbuzz, end=",")
