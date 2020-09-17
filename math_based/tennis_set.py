def tennisSet(score1, score2):
    # if scores are higher than 7, return false
    # if score1 or score2 equals 5, check if score1 or score2 equals 7. if yes, return true, else return false
    # if score1 or score2 does not equal 5, check if score1 or score2 equals 6. if yes, return true, if no return false

    if score1 + score2 == 0:

        return False

    if score1 and score2 < 8:

        if score1 == 7:
            if score2 < 7 and score2 >= 5:
                return True
            else:
                return False

        if score2 == 7:
            if score1 < 7 and score1 >= 5:
                return True
            else:
                return False

        if score1 == 6:
            if score2 < 5:
                return True
            else:
                return False

        if score2 == 6:
            if score1 < 5:
                return True
            else:
                return False

    if score1 or score2 > 7:
        return False
