def shapeArea(n):
    prod_curr = n*n
    prod_prev = (n-1) * (n-1)

    return prod_curr + prod_prev

    # if n == 2
    # 2*2 + 1*1 = 5

    # if n == 4
    # 4 * 4 + 3*3 = 25
