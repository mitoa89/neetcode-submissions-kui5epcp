# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # bst이니까 값을 알면 중간값을 찾으면되지않나
        #post order
        def dfs(node):
            if not node:
                return None
            
            if node.val == p.val or node.val == q.val:
                return node

            left = dfs(node.left)
            right = dfs(node.right)
            has = left and right
            if has:
                return node
            if left:
                return left
            if right:
                return right

        return dfs(root)



        