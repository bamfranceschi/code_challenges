def isInfiniteProcess(a, b):

    while a != b:

        if a > b:
            return True
        if b - a == 1:
            return True

        a += 1
        b -= 1
        print(a, b)

    return False
