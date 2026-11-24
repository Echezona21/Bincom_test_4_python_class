#Generate a fibonacci series up to n terms
n = int(input("Enter the number of terms: "))

def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

print (fibonacci_series(n)) #prints the fibonacci series up to n terms input by the user