# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dic = defaultdict()

        curr = head
        i = 0
        while curr:
            dic[i] = curr
            curr = curr.next
            i += 1

        curr = head
        
        length = i
        i = 1
        print(dic)

        while i < length - i:
            print(length -i, i)
            curr.next = dic[length - i]

            curr = curr.next
            curr.next = dic[i]

            curr = curr.next
            i += 1

        if i is length - i:
            curr.next = dic[i]
            curr = curr.next

        curr.next = None
    

        return 