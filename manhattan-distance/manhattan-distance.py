import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    c=0
    for i in range(len(x)):
        for j in range(len(x)):
            if i == j:
                c= c+abs(x[i]-y[j])
    return c
            