def checkPalindrome(inputString):

    reverse_input = inputString[::-1]

    print(reverse_input)

    if inputString == reverse_input:
        return True
    else:
        return False
