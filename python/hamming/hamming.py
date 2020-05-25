def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('inputs different length')
    dist = 0
    for i, x in zip(strand_a, strand_b):
        if i != x:
            dist += 1
    return dist
