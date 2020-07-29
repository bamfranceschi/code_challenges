def first_not_repeating_character(s):
    #everything is lowercase
    # return first unique
    # if no first unique, return '_'

    # set up a dict
    char_dict = {}
    uniques = set()
    idx_uniques = set()

    # loop over string and count occurrences of each char
    for char in s:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    # for chars with occurrence of 1, add to the uniques set
    for key in char_dict:
        if char_dict[key] == 1:
            uniques.add(key)
    # if there are no uniques, return '_'
    if len(uniques) == 0:
        return '_'
    # loop over string, grab idx of unique chars
    for idx, char in enumerate(s):
        if char in uniques:
            idx_uniques.add(idx)
    # sort unique idx to be able to grab lowest idx, aka first occurence of unique char
    idx_un_sorted = sorted(idx_uniques)
    result = s[idx_un_sorted[0]]

    return result

    # return lower index
