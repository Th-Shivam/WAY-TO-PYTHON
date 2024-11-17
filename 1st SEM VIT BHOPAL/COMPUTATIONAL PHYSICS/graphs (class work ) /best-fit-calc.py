import numpy as np
import matplotlib.pyplot as plt

# Sample data (x and y values)
x = np.array([1, 2, 3, 4, 5])  # Input values
y = np.array([2, 4.1, 6.5, 9.4, 14.3])  # Output values (observed data)

# Fit a second-degree polynomial (quadratic)
coefficients = np.polyfit(x, y, 2)

# Coefficients for the equation: y = a + bx + cx^2
c, b, a = coefficients

# Print the values of a, b, and c
print(f"Coefficient a: {a}")
print(f"Coefficient b: {b}")
print(f"Coefficient c: {c}")

# Print the best-fit equation
print(f"\nBest-fit equation: y = {a} + {b}x + {c}x^2")

# Calculate the best-fit line (predicted y values)
y_fit = a + b * x + c * x**2

# Plot the data points and the best-fit curve
plt.scatter(x, y, color='red', label='Data points')
plt.plot(x, y_fit, color='blue', label='Best fit curve')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Best Fit Line (y = a + bx + cx^2)')
plt.show()
