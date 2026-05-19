# def gradient_descent_quadratic(a, b, c, x0, lr, steps):
#     """
#     Return final x after 'steps' iterations.
#     """
    
#     x = x0
#     for i in range(steps):
#         grad = 2 * a * x + b  
#         x = x - lr * grad      
#     return x
def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    x = x0
    for _ in range(steps):
        x -= lr * (2*a*x + b)
    return x