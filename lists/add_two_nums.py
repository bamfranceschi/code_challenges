class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list = list()
        l2_list = list()
        # need to iterate over both lists,
        while l1 is not None and l2 is not None:
            # adding each node to set at the 0th index
            l1_list.insert(0, l1)
            l2_list.insert(0, l2)
        # that way, they end up correctly reversed
        # then concatenate each set
        l1_list_value = "".join(l1_list)
        l2_list_value = "".join(l2_list)
        # add concatenated values together
        end_result = l1_list_value + l2_list_value
        # then split result into three elements
        end_result_string = str(end_result)
        end_result_array = end_result_string.split("")
        # reverse elements in place
        end_result_array[::-1]
        end_result_list = ListNode(None)
        current_new = end_result_list
        # iterate over the three elements and make them into a linked list
        for element in end_result_array:

            if current_new.next is not None:
                # add them to ll
                current_new.next = ListNode(element)
                current_new = current_new.next
            else:
                current_new.next = None

        return end_result_list.next
