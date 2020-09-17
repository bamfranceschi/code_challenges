def phoneCall(min1, min2_10, min11, s):
    # subtract min1 from s, add 1 min
    # subtract min2-10 * 9 from s, add 9 min (if new total is greater than min2_10 * 9)
    # else: new total divided by min2_10, add that number to total min
    # new total divided by min11, add that number to total min

    cents_left = s - min1
    call_length = 1

    if cents_left >= (min2_10 * 9):
        call_length += 9
        cents_left = cents_left - (min2_10 * 9)

        call_length += cents_left // min11
        return call_length

    else:
        call_length += cents_left // min2_10
        return call_length
