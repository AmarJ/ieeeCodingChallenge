def find_minimum_loss(a):
    min_so_far = 0
    for i in xrange(len(a)):
        for j in xrange(i + 1, len(a)):
            check = a[i] - a[j]
            if check > 0 and (not min_so_far or check < min_so_far):
                min_so_far = check
    return min_so_far
