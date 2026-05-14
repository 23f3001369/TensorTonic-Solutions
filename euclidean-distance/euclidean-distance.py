import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # c=0
    # for i in range(len(x)):
    #     for j in range(len(x)):
    #         if len(x) == len(y):
    #             if i == j:
    #                 c = c+(x[i]-y[j])**2
    #         else:
    #             c = none
    # return c**(1/2)

    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)

    
    if x.shape != y.shape:
        raise ValueError("Vectors must be the same length")

    
    return float(np.sqrt(np.sum((x - y) ** 2)))
