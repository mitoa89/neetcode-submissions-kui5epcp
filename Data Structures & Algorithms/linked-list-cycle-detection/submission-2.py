# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr1 = head
        curr2 = head
        while curr1 and curr2:
            print(curr1.val, curr2.val)
            curr1 = curr1.next
            if curr2.next:
                curr2 = curr2.next.next
            else:
                break
            if curr1 == curr2:
                return True
        return False