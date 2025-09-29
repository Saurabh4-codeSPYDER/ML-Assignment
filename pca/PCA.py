# Function to calculate variance of data projected onto a unit vector
def variance_on_unit_vector(points, u, v):
    length = (u**2 + v**2) ** 0.5
    u, v = u / length, v / length

    projections = []
    for (x, y) in points:
        alpha = x * u + y * v  
        projections.append(alpha)


    mean_alpha = sum(projections) / len(projections)
    variance = sum((alpha - mean_alpha) ** 2 for alpha in projections) / len(projections)

    return variance


# Covariance matrix computation
def covariance_matrix(points):
    n = len(points)
    mean_x = sum(p[0] for p in points) / n
    mean_y = sum(p[1] for p in points) / n

    centered = [(x - mean_x, y - mean_y) for (x, y) in points]


    sxx = sum(p[0]*p[0] for p in centered) / (n-1)
    syy = sum(p[1]*p[1] for p in centered) / (n-1)
    sxy = sum(p[0]*p[1] for p in centered) / (n-1)

    return [[sxx, sxy],
            [sxy, syy]]


# find eigenvector with largest eigenvalue
def principal_eigenvector(matrix, iterations=1000):
    import random
    b = [random.random(), random.random()]

    norm = (b[0]**2 + b[1]**2) ** 0.5
    b = [b[0]/norm, b[1]/norm]

    for _ in range(iterations):
        new_b = [
            matrix[0][0]*b[0] + matrix[0][1]*b[1],
            matrix[1][0]*b[0] + matrix[1][1]*b[1]
        ]
        norm = (new_b[0]**2 + new_b[1]**2) ** 0.5
        b = [new_b[0]/norm, new_b[1]/norm]

    return b


points = [
    (2.5, 2.4),
    (0.5, 0.7),
    (2.2, 2.9),
    (1.9, 2.2),
    (3.1, 3.0)
]

u, v = 1, 2
result = variance_on_unit_vector(points, u, v)
print("Variance along direction (1,2):", result)

cov = covariance_matrix(points)
print("\nCovariance matrix:")
for row in cov:
    print(row)

best_u, best_v = principal_eigenvector(cov)
print("\nBest direction (u,v):", (best_u, best_v))

best_var = variance_on_unit_vector(points, best_u, best_v)
print("Maximum variance along best direction:", best_var)
