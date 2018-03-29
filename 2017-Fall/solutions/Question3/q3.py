def find_number_of_repeats(substr, s):
    if s == '':
        return 0
    if len(s) < len(substr) and s in substr:
        return 1
    for i in xrange(len(substr) - 1):
        if s.startswith(substr[i:]):
            count = 1
            remaining_s = s[len(substr) - i:]
            while len(remaining_s) >= len(substr):
                if remaining_s.startswith(substr):
                    count += 1
                    remaining_s = remaining_s[len(substr):]
                else:
                    break
            if len(remaining_s) == 0:
                return count
            if substr.startswith(remaining_s):
                count += 1
                return count
    return -1
