INFINITY = 9999999

def sqrt_by_long_division(n: int) -> int:
    """
    Calculate the integer square root of a number using the long division method.
    
    Args:
        n (int): The number to find the square root of.
    
    Returns:
        int: The integer part of the square root.
    """
    if n < 0:
        raise ValueError("Square root is not defined for negative numbers.")

    segments = [0] * 10  # Holds digit pairs from the number
    num_segments = 0

    # Break the number into 2-digit segments (right to left)
    while n > 0:
        segments[num_segments] = n % 100
        n //= 100
        num_segments += 1

    num_segments -= 1  # Last valid index

    quotient = 0
    divisor = 0
    dividend = 0

    # Start long division from most significant 2-digit segment
    for i in range(num_segments, -1, -1):
        dividend = dividend * 100 + segments[i]
        remainder = INFINITY
        unit_digit = 0

        # Find the best digit to append to current quotient
        for d in range(10):
            candidate = (divisor * 10 + d) * d
            if dividend >= candidate and dividend - candidate <= remainder:
                remainder = dividend - candidate
                unit_digit = d

        quotient = quotient * 10 + unit_digit
        divisor = quotient * 2
        dividend = remainder

    return quotient


# Driver code
if __name__ == "__main__":
    try:
        x = int(input("Enter a non-negative integer: "))
        print(f"Square root (integer part) = {sqrt_by_long_division(x)}")
    except ValueError as ve:
        print(f"Error: {ve}")