def fibonacci_iterative(n):
    if n <= 1:
        return n

    a, b = 0, 1

    for i in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    print("Fibonacci using iteration:", fibonacci_iterative(n))
    print("Fibonacci using recursion:", fibonacci_recursive(n))

    print("\nTime and space complexity:")
    print("Iterative: Time O(n), Auxiliary Space O(1)")
    print("Recursive: Time O(2^n), Auxiliary Space O(n)")
