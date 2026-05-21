import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    y: array-like of class labels
    """
    # Convert to numpy array
    y = np.array(y)

    # Count occurrences of each class
    values, counts = np.unique(y, return_counts=True)

    # Probabilities
    probs = counts / counts.sum()

    # Use np.where to avoid log(0)
    entropy = -np.sum(probs * np.log2(np.where(probs > 0, probs, 1)))

    return entropy