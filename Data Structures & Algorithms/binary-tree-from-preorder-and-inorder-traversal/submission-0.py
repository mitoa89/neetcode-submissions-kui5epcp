# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        #[1,2,3,4]
        #[2,1,3,4]
        indices = {val : idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0
        def build(left, right):
            if left > right:
                return None

            rootval = preorder[self.pre_idx]
            node = TreeNode(rootval)
            self.pre_idx += 1
            mid = indices[rootval]
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            return node
            
        return build(0, len(inorder) - 1)
