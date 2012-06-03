def online_median(x, init_median=0):
    """Calculates the median of a series x """
    median = [init_median]
    for e in x:
        median.append(median[-1] + (1./len(median)*(e-median[-1])))
    return median 
