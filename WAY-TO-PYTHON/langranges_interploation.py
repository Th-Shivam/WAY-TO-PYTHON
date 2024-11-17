# Lagrange Interpolation Function
def lagrange_interpolation(x_points, y_points, x):
    # Number of data points
    n = len(x_points)
    
    # Initialize interpolated value
    result = 0.0

    # Apply the Lagrange interpolation formula
    for i in range(n):
        # Start with the i-th term
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        
        # Add the term to the result
        result += term
    
    return result

# Sample data points (x, y)
x_points = [5, 6, 9, 11]
y_points = [12, 13, 14, 16]

# Interpolate at x = 10
x_value = 10
interpolated_value = lagrange_interpolation(x_points, y_points, x_value)

print(f"The interpolated value at x = {x_value} is {interpolated_value}")

