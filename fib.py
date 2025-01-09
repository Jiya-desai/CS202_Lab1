'''printing the nth fibonacci number'''

def fibonacci(n):
    '''this is a function'''
    # for invalid input:
    if n <= 0:
        print("Please enter a positive integer greater than 0.")
        return
    # base case initialisation:
    a, b = 0, 1
    # next fib number:
    for _ in range(2, n + 1):
        a, b = b, a + b

    # base case
    if n == 1:
        print(f"The {n}th Fibonacci number is: {a}")
    else:
        print(f"The {n}th Fibonacci number is: {b}")


num = int(input("Enter 'n' to print the nth Fibonacci number: "))
fibonacci(num)
