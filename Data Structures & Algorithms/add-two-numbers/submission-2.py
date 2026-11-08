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

        while node1 and node2:
            val = (node1.val + node2.val + carry) % 10
            carry = (node1.val + node2.val + carry)//10

            node.next = ListNode(val)
            node = node.next

            node1 = node1.next
            node2 = node2.next
        
        while node1:
            val = (node1.val + carry) % 10
            carry = (node1.val + carry) // 10

            node.next = ListNode(val)
            node = node.next
            node1 = node1.next
        
        while node2:
            val = (node2.val + carry) % 10
            carry = (node2.val + carry) // 10

            node.next = ListNode(val)
            node = node.next
            node2 = node2.next
        
        if carry:
            node.next = ListNode(carry)
        
        return result.next

