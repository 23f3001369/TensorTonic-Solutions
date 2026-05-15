import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    import numpy as np

def expected_value_discrete(x, p):
    """
    Compute the expected value of a discrete random variable.
    Returns: float expected value
    """
    x = np.array(x, dtype=float)
    p = np.array(p, dtype=float)

    if len(x) != len(p):
        raise ValueError("x and p must have the same length")

    if np.any(p < 0):
        raise ValueError("Probabilities must be non-negative")
    if not np.isclose(np.sum(p), 1.0):
        raise ValueError("Probabilities must sum to 1")

    return float(np.sum(x * p))

