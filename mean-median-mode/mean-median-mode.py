import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Mean
    mean_val = np.mean(x)

    # Median
    median_val = np.median(x)

    # Mode 
    # counts = Counter(x)
    # max_count = max(counts.values())
    # mode_val = min([k for k, v in counts.items() if v == max_count])
    
    counts = Counter(x)
    max_count = max(counts.values())
    mode_val = None

    for k, v in counts.items():
        if v == max_count:
            if mode_val is None or k < mode_val:
                mode_val = k

    return mean_val, median_val, mode_val

   