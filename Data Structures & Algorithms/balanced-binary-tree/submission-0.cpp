/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isB = true;
    bool isBalanced(TreeNode* root) {
        depth(root);
        return isB;
    }

    int depth(TreeNode* root)
    {
        if (root == nullptr)
            return 0;
        
        auto leftDepth = depth(root->left);
        auto rightDepth = depth(root->right);
        
        if (std::abs(leftDepth - rightDepth) > 1)
            isB = false;
        return 1 + max(leftDepth, rightDepth);
    };

};
