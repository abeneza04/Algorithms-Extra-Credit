"""
Problem: Need to implement a function to compute the nth Fibonacci number using both iterative and recursive approaches.
Result is in the README
"""
# Iterative solution
def fibonacci_iterative(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

print("Iterative Fibonacci (first 10 numbers):")
print(fibonacci_iterative(10))

# Recurisve solutuion

def fibonacci_recursive_seq_return(n):
    result = []
    for i in range(n):
        result.append(fibonacci_recursive(i))
    return result
    
def fibonacci_recursive(n):
    if n <= 1: # base case
        return n
    
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2) 
    # This is the recursive case
    # The function calls itself with the two preceding numbers until it reaches the base case.

print("\nRecursive Fibonacci (first 10 numbers):")
print(fibonacci_recursive_seq_return(10))