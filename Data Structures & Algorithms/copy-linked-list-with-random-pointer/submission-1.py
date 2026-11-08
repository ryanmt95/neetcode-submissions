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
        
        dummy = Node(0)
        newNode = dummy
        node = head
        nodeMap = dict()
        newNodePointer = dummy

        while node:
            temp = Node(node.val)
            nodeMap[node] = temp

            newNode.next = temp
            newNode = newNode.next
            node = node.next
        
        for node, newNode in nodeMap.items():
            oldRandomNode = node.random

            if oldRandomNode in nodeMap:
                newRandomNode = nodeMap[oldRandomNode]
                newNode.random = newRandomNode

        return dummy.next
