# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree2(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)

        dfs(root)
        return self.diameter

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        node = root
        stack = [root]
        maxSize = 0
 
        while stack:
            node = stack.pop()
 
            maxSize = max(maxSize, self.maxDepth(node.left) + self.maxDepth(node.right))
 
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)

        return maxSize

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
 
        node = root
        stack = [(root, 1)]
        maxSize = 0
 
        while stack:
            node, depth = stack.pop()
 
            maxSize = max(maxSize, depth)
 
            if node.left is not None:
                stack.append((node.left, depth+1))
            if node.right is not None:
                stack.append((node.right, depth+1))
        return maxSize
