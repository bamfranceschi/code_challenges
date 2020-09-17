def metroCard(lastNumberOfDays):
    # if lastNumberOfDays is 30:
    # the answer can only be [31]
    # if lastNumberOfDays is 31:
    # the answer can only be [28, 30, 31]
    # if lastNumberOfDays is 28:
    # the answer can only be [31]

    if lastNumberOfDays == 28 or lastNumberOfDays == 30:
        return [31]

    if lastNumberOfDays == 31:
        return [28, 30, 31]
