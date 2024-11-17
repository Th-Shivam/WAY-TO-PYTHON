def cross_product(vector_a, vector_b):
    if len(vector_a) == 3 and len(vector_b) == 3:
        cross_prod = [
            vector_a[1] * vector_b[2] - vector_a[2] * vector_b[1],
            vector_a[2] * vector_b[0] - vector_a[0] * vector_b[2],
            vector_a[0] * vector_b[1] - vector_a[1] * vector_b[0]
        ]
        return cross_prod
    else:
        raise ValueError("Both vectors must be 3-dimensional")

# Example usage:
vector1 = [1, 0, 0]
vector2 = [2, 0, 0]
result = cross_product(vector1, vector2)
print("Cross product:", result)


