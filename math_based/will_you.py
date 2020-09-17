def willYou(young, beautiful, loved):

    if young == True and beautiful == True:
        if loved == False:
            return True
        else:
            return False

    if young == False or beautiful == False:
        if loved == True:
            return True
        else:
            return False
