def print_fibonacci(n):
    fibonacci_list = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_list.append(a)
        a, b = b, a + b
    print(fibonacci_list)

# Example usage:
print_fibonacci(9)
