def adjacentElementsProduct(inputArray):
    # loop over the array, storing multiplication values between adjacent elements in a set
    # sort set reversed, return first element from set

    s = set()

    for i in range(len(inputArray)-1):
        product = inputArray[i] * inputArray[i+1]
        s.add(product)

    s_sorted = sorted(s, reverse=True)

    return s_sorted[0]
