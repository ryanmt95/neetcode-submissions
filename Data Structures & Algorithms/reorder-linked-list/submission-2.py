# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# [0, 1, 2, 3, 4, 5] -> 3
# list1: 0 -> 1 -> 2 -> 3, list2: 5 -> 4 -> 3
# [0, 1, 2, 3, 4, 5, 6] -> 3

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        node = slow.next
        slow.next = None

        prev = None

        while node:
            temp = node 
            node = node.next

            temp.next = prev
            prev = temp
        
        node1 = head
        node2 = prev

        while node1 and node2:
            next1 = node1.next
            next2 = node2.next

            node1.next = node2
            node2.next = next1

            node1 = next1
            node2 = next2
        
        
        return


