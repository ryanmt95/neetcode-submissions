# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # if list1 is None:
        #     return list2
        # if list2 is None:
        #     return list1
        
        result = ListNode(0)
        head = result
        node1 = list1
        node2 = list2

        while node1 and node2:
            if node1.val < node2.val:
                head.next= node1 
                node1 = node1.next
                head = head.next
            
            else:
                head.next = node2
                node2 = node2.next
                head = head.next
        
        if node1:
            head.next = node1
        
        if node2:
            head.next = node2
        
        return result.next