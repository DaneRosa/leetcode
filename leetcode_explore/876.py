'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

'''

from math import ceil
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mapped = []
        n = 0
        while head:
            mapped.append(head)
            n += 1
            head = head.next
        k = n // 2 if n % 2 else ceil(n/2)
        return mapped[k]