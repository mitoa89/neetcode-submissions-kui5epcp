# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        nth = length - n
        i = 0
        curr = head
        dummy = ListNode
        dummy.next = head
        prev = dummy
        while curr:
            if i == nth:
                prev.next = curr.next
                break
            i+=1
            prev = curr
            curr = curr.next

        return dummy.next