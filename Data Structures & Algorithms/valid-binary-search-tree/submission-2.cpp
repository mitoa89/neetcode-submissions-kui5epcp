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
    bool isValidBSTSub(TreeNode* root, long minVal, long maxVal) {

        if (root == nullptr)
            return true;

        if(!(minVal < root->val && root->val < maxVal))
            return false;

        return isValidBSTSub(root->left, minVal, root->val) && isValidBSTSub(root->right, root->val, maxVal);
    }
    bool isValidBST(TreeNode* root) {
        return isValidBSTSub(root, LONG_MIN, LONG_MAX);
    }
};
