def find_number_of_repeats(substr, s):
    if s == '':
        return 0
    if len(s) <= len(substr) and s in substr:
        return 1
    front_indices = []
    back_indices = []
    for i in xrange(len(substr) - 1):
        if s.startswith(substr[i:]):
            front_indices.append(len(substr) - i)
    for i in xrange(1, len(substr) + 1):
        if substr.startswith(s[-i:]):
            back_indices.append(len(s) - i)
    for f in front_indices:
        for b in back_indices:
            if f == b:
                return 2
            if (b - f) % len(substr) == 0:
                count = 2
                check = s[f:b]
                while check:
                    if check.startswith(substr):
                        count += 1
                        check = check[len(substr):]
                    else:
                        break
                    if not check:
                        return count

    return -1
