#include <iostream>
#include <vector>

#include "solution.hpp"

int main()
{   
    TreeNode * input = new TreeNode(1);
    input->right = new TreeNode(2);
    input->right->left = new TreeNode(3);

    Solution solver;
    std::vector<int> output = solver.inorderTraversal(input);

    for (int val : output)
        std::cout << val << " ";

    return 0;
}