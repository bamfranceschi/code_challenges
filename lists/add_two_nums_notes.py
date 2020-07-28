class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list = []
        l2_list = []
        # need to iterate over both lists,
        while l1 is not None:
            l1_list.insert(0, str(l1.val))
            l1 = l1.next
        while l2 is not None:
            # adding each node to set at the 0th index
            l2_list.insert(0, str(l2.val))
            l2 = l2.next
        # that way, they end up correctly reversed
        # then concatenate each set
        l1_list_value = "".join(l1_list)
        l2_list_value = "".join(l2_list)
        # add concatenated values together
        end_result = str(int(l1_list_value) + int(l2_list_value))[::-1]
        # then split result into three elements
        # reverse elements in place
        end_result_array = []

        for num in end_result:
            end_result_array.append(ListNode(num))
        for node in range(len(end_result_array)):
            if node != len(end_result_array)-1:
                end_result_array[node].next = end_result_array[node+1]

        return end_result_array[0]
