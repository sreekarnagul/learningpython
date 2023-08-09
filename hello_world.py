
def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        print(f"Returning {n}+ fib{n-1} + fib{n-2}")
        return n+fib(n-1) + fib(n-2)

inputNumber = int(input("Enter a number to calculate Fibonacci:"));
print(f"Calculating Fibonacci of number:{inputNumber}")
value = fib(inputNumber)
print(f"Fibonacci of {inputNumber} is {value}")
