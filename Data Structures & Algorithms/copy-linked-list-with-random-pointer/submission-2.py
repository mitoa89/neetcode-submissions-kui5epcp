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
        if not head:
            return None
        temp_head = Node(head.val)
        curr_temp = temp_head    

        curr = head
        dic = {}

        while curr:
            dic[curr] = curr_temp
            
            if curr.next:
                curr_temp.next = Node(curr.next.val)
                curr_temp = curr_temp.next
            curr = curr.next
        
        curr = head
        curr_temp = temp_head
        while curr:
            if curr.random:
                curr_temp.random = dic[curr.random]
            
            curr_temp = curr_temp.next
            curr = curr.next

        return temp_head