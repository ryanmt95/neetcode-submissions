# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        node1 = l1
        node2 = l2
        result = ListNode(0)
        node = result

        while node1 or node2:
            node1val = node1.val if node1 else 0
            node2val = node2.val if node2 else 0

            val = (node1val + node2val + carry) % 10
            carry = (node1val + node2val + carry)//10

            node.next = ListNode(val)
            node = node.next

            if node1:
                node1 = node1.next
            if node2:
                node2 = node2.next
        
        if carry:
            node.next = ListNode(carry)
        
        return result.next

