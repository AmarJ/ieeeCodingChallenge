def find_minimum_loss(a):
    values = {}
    for i, v in enumerate(a):
        if v not in values:
            values[v] = 0
        values[v] = i
    a = sorted([(v, values[v]) for v in values], reverse=True)
    min_loss = 0
    for i in xrange(len(a) - 1):
        check = a[i][0] - a[i + 1][0]
        if a[i + 1][1] > a[i][1] and (not min_loss or check < min_loss):
            min_loss = check
    return min_loss
