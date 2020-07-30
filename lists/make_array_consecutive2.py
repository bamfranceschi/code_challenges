def makeArrayConsecutive2(statues):
    # sort from lowest to highest
    sorted_statues = sorted(statues)
    statues_needed = 0
    # for loop over array
    for idx in range(len(sorted_statues)-1):
        # compare element and element + 1
        # determine difference between the two elements
        diff = (sorted_statues[idx + 1] - sorted_statues[idx]) - 1
        # increment statue counter with the difference
        statues_needed += diff

    return statues_needed
