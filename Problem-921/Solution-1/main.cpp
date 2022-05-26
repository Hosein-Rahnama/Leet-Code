#include <iostream>
#include <string>

#include "solution.hpp"

int main()
{
    std::string input = "())";

    Solution solver;
    int output = solver.minAddToMakeValid(input);

    std::cout << output << std::endl;

    return 0;
}