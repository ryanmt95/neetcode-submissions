"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        copyDummy = Node(0)
        copyNode = copyDummy
        node = head
        nodeMap = dict()

        while node:
            copyNewNode = Node(node.val)
            copyNode.next = copyNewNode
            nodeMap[node] = copyNewNode

            node = node.next
            copyNode = copyNode.next

        copyNode = copyDummy.next
        node = head

        while node:
            if node.random:
                copyRandomNode = nodeMap[node.random]
                copyNode.random = copyRandomNode
            
            node = node.next
            copyNode = copyNode.next
        
        return copyDummy.next
