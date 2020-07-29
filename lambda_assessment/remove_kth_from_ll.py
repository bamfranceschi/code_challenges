# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def remove_kth_from_end(head, k):
    # we are given a linked list
    # we are given k, which represents the position-starting from the end- of the element that we need to remove
    # we'll need to reassign the prior element's .next to k's .next
    # we want to return the head of the altered linked list

    # capture the original head in variable
    current_head = head
    # starts at 1 since we start at head
    length_counter = 1

    # return the LL since we aren't deleting any nodes
    if k == 0:
        return head
    # determine length of LL - need to traverse
    while current_head.next:
        # use this to determine length of LL
        length_counter += 1
        current_head = current_head.next

    # return the LL since there isn't a kth element
    if k > length_counter:
        return head

    # return head.next since we're deleting the 0th element in LL
    if k == length_counter:
        head = head.next
        return head

    # subtract k from length to identify kth element
    kth_element = length_counter - k
    k_counter = 1
    prev = head
    current_head = head.next

    # traversing LL until we get to kth element
    while k_counter < kth_element:
        k_counter += 1
        prev = current_head
        current_head = current_head.next

    #reassign .nexts
    prev.next = current_head.next
    # return head
    return head
