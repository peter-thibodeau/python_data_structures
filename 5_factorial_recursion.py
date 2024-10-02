print('GET FACTORIAL USING RECURSION')
def factorial(n):
    if n == 0:
        return 1 # the factorial of zero is one (base case)
    else:
        return n * factorial(n-1)

n = int(input('Enter a non-negative number: '))
if n < 0:
    n = int(input('Enter a non-negative number: '))

f = factorial(n)
print(f"The factorial for the number {n} is {f}")
