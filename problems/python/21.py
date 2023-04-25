'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

expected: 
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # node to hold merged list
        x = ListNode(0)
        # set current var to track the current node in merged list
        current = x

        # loop through both lists as long as there are still nodes to merge
        while list1 and list2:
            # choose the smaller of the 2 nodes, add it to merged list and advance
            if list1.val <= list2.val:
                # add val to list 
                current.next = list1
                # advance past the added value
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            # move the current node of the merged list to the node that was just added to prevent overweite
            current=current.next
        
        # add the remaing nodes from list1 or list2 to the end of the merged list
        current.next = list1 or list2

        # return the reference to the start of the merged list (skipping held node)
        return x.next
        



        



