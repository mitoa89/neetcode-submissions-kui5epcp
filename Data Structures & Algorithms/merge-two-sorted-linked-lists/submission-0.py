# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        node1 = list1
        node2 = list2
        prev = None
        head = None
        while node1 or node2:
            if node1 and node2:
                if node1.val <= node2.val:
                    cur = node1
                    node1 = node1.next
                else:
                    cur = node2
                    node2 = node2.next
            elif node1:

                cur = node1
                node1 = node1.next
            elif node2:
                cur = node2
                node2 = node2.next
            if not head:
                head = cur

            if prev:
                prev.next = cur
            prev = cur

        return head