def uncover_spy(n, trust):

    # trust is an array of array-pairs
    # see who is trusted, /// look at the 1st index of each pair
    # count how many people trust those who are trusted /// count how many times a given number occurs in the 1st index
    # if the count is n-1, then everyone trusts the spy

    # do we store the parent array in a dict for easy access?
    # we have to look at each pair
    # if we iterate over the dict, can we pull out each pair to look at?
    # maybe we use a dict to store the 1st elements in each pair and their occurences in the pairs

    pairs_dict = {}
    trusted_dict = {}
    trusters_set = set()
    # populated refrence dict with all available pairs
    for idx, pair in enumerate(trust):
        pairs_dict[idx] = pair

    # iterate over dict values
    for key in pairs_dict:

        # populating the trusted people, aka 1st elements
        trusted = pairs_dict[key][1]
        # populating the trusting people, aka 0th elements
        trusters_set.add(pairs_dict[key][0])

        # incrementing trust count for each trusted person
        if trusted not in trusted_dict:
            trusted_dict[trusted] = 1
        else:
            trusted_dict[trusted] += 1

    # looping through all people, aka numbers, who are trusted
    for key in trusted_dict:
        # if the person is also not a truster
        if key not in trusters_set:
            # if their trust count is equal to the population - 1
            if trusted_dict[key] == n-1:
                # that's our spy!
                return key
            else:
                return -1
        else:
            return -1
