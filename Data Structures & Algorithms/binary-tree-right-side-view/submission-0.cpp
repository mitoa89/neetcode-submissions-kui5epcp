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
    vector<int> rightSideView(TreeNode* root) {
        std::vector<int> rights;      
        auto dfs = [&](auto&&self, TreeNode* node, int level = 0)  -> void{
            if (node == nullptr)
                return;
            if(rights.size() == level)
            {
                rights.push_back(node->val);
            }

            self(self, node->right, level +1);
            self(self, node->left, level+1);
        };

        dfs(dfs, root);
        return rights;
    }
};
