# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        result = ListNode(0)
        node = result

        while list1 or list2:
            list1Val = list1.val if list1 else float('inf')
            list2Val = list2.val if list2 else float('inf')

            if list1Val < list2Val:
                node.next = list1
                
                list1 = list1.next
                node = node.next
            
            else:
                node.next = list2 

                list2 = list2.next
                node = node.next
        
        return result.next
        