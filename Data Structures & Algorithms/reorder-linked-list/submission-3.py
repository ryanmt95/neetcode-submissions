# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [0, 1, 2, 3, 4, 5], slow = 3
# [0, 1, 2, 3, 4, 5, 6], slow = 3

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        secondList = slow.next
        slow.next = None

        previous = None
        curr = secondList

        while curr:
            temp = curr
            curr = curr.next

            temp.next = previous
            previous = temp

        second = previous
        first = head

        result = ListNode(0)
        node = result

        while first or second:
            if first:
                node.next = first
                first = first.next
                node = node.next
            
            if second:
                node.next = second
                second = second.next
                node = node.next
        
        return 