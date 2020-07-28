def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

    result = {}

    # loop through strs list:
    for word in strs:
        # sort the current word
        sorted_word = ''.join(sorted(word))
        # if it's the first word to match this sort
        if sorted_word not in result:
            result[sorted_word] = [word]
        else:
            result[sorted_word].append(word)

    return list(result.values())
