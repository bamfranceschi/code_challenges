""""
Find all the pairs of two integers in an unsorted array that sum up to a given S. For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7, your program should return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7
"""

# looking for complements
# integers can be pos or neg
# expected output is two d array


def find_two_pairs(arr, s):
    # use dict
    # loop over existing array and subtract integer from s
    # save that in dict

    #complements = {}
    comp_list = []

    for a in arr:
        comp = s - a
        #complements[a] = comp

        if comp in arr:
            comp_list.append([a, comp])

        # print(comp_list)

    return comp_list


ex_arr = [3, 5, 2, -4, 8, 11]

print(find_two_pairs(ex_arr, 7))
