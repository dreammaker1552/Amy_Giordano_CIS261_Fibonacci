def fibonacci(n):
    # Initialize the first two numbers in the sequence
    fib_series = [0, 1]

    # Generate the sequence up to the nth number
    for i in range(2, n + 1):
        # Calculate the next number in the sequence as the sum of the two preceding ones
        next_num = fib_series[i-1] + fib_series[i-2]
        # Add the next number to the sequence
        fib_series.append(next_num)

    # Return the generated sequence
    return fib_series

fib_series = fibonacci(16)
print(fib_series)

