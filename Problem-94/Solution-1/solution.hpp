#include <vector>

struct TreeNode
{
    int val;
    TreeNode * left;
    TreeNode * right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int val) : val(val), left(nullptr), right(nullptr) {}
    TreeNode(int val, TreeNode * left, TreeNode * right) : val(val), left(left), right(right) {}
};

class Solution
{
public:
    std::vector<int> inorderTraversal(TreeNode * root);
private:
    void inorderTraversalHelper(TreeNode * root, std::vector<int> & inorderTraversalNodes);
};

std::vector<int> Solution::inorderTraversal(TreeNode * root)
{
    std::vector<int> inorderTraversalNodes;
    inorderTraversalHelper(root, inorderTraversalNodes);
    return inorderTraversalNodes;
}

void Solution::inorderTraversalHelper(TreeNode * root, std::vector<int> & inorderTraversalNodes)
{
    if (root == nullptr)
    {
        return;
    }
    inorderTraversalHelper(root->left, inorderTraversalNodes);
    inorderTraversalNodes.push_back(root->val);
    inorderTraversalHelper(root->right, inorderTraversalNodes);
}