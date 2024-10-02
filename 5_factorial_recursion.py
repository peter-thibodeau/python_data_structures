print('GET FACTORIAL USING RECURSION')
def factorial(n):
    if n < 0:
        print('Error! enter non-negative numbers only')
        exit()
    elif n == 0:
        return 1 # the factorial of zero is one which is the base case
    else:
        return n * factorial(n-1)

f = factorial(0)
print(f"The factorial for the number {0} is {f}")

f = factorial(5)
print(f"The factorial for the number {5} is {f}")

f = factorial(99)
print(f"The factorial for the number {99} is {f}")
