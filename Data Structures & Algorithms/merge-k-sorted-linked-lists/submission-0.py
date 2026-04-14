# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode(1000)
        curr = dummy
        while curr:
            min_val = 1000
            next_node = None
            selected = -1
            for i, node in enumerate(lists):
                if node.val <= min_val:
                    min_val = node.val
                    next_node = node
                    selected = i
            
            if selected >= 0:
                if next_node:
                    lists[selected] = next_node.next
                if not lists[selected]:
                    del lists[selected]
                
            curr.next = next_node
            curr = curr.next

            #print(curr.val)

        return dummy.next