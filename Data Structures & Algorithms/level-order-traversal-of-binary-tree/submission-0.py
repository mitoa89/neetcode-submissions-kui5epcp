# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()

        q.append((0, root))
        curr_level = 0
        new_list = []
        res = []
        while q:
            level, node = q.popleft()

            if level == curr_level:
                new_list.append(node.val)
            else:
                res.append(new_list[:])
                new_list = [node.val]

            curr_level = level
            if node.left:
                q.append((level+1, node.left))
            if node.right:
                q.append((level+1, node.right))

        res.append(new_list)
        return res

