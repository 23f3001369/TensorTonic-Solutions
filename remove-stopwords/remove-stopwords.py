def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    stopwords = set(stopwords)  
    # return [t for t in tokens if t not in stopwords]
    s = []
    for t in tokens:
        if t not in stopwords:
            s.append(t)
    return s
