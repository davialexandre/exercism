
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('It is not possible to calculate the distance of strands with different sizes')

    distance = 0

    i = 0
    while i < len(strand_b):
        if strand_a[i] != strand_b[i]:
            distance += 1

        i += 1

    return distance