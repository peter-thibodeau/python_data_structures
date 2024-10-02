print('GET FIBONACCI NUMBER USING RECURSION')

def fibonacci(n):
    if n <= 0:
        print("Error! positive whole numbers greater than zero only.")
    elif n == 1: # the fibonacci number for 1 is 0 (no formula necessary)
        return 0
    # Second fibonacci number is 1
    elif n == 2: # the fibonacci number for 2 is 1 (no formula necessary)
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# test cases
x = 1
f = fibonacci(x)
print(f"The factorial for the number {x} is {f}")

x = 10
f = fibonacci(x)
print(f"The factorial for the number {x} is {f}")

x = 5
f = fibonacci(x)
print(f"The factorial for the number {x} is {f}")

x = 20
f = fibonacci(x)
print(f"The factorial for the number {x} is {f}")

