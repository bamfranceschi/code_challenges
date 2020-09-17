def knapsackLight(value1, weight1, value2, weight2, maxW):

    chest_weight = weight1 + weight2

    if maxW >= chest_weight:
        return value1 + value2

    if maxW < weight1 and maxW < weight2:
        return 0
    if maxW < chest_weight:
        if weight1 and weight2 < maxW:
            return max(value1, value2)
        elif weight1 <= maxW:
            return value1
        elif weight2 <= maxW:
            return value2
