#include <string>

class Solution
{
public:
    int minAddToMakeValid(std::string parenthesesString);
};

int Solution::minAddToMakeValid(std::string parenthesesString)
{
    int openingParentheses = 0;
    int closingParentheses = 0;
    for (char parenthesis : parenthesesString)
    {
        if (parenthesis == '(')
        {
            openingParentheses += 1;
        }
        else
        {
            if (openingParentheses > 0)
            {
                openingParentheses -= 1;
            }
            else
            {
                closingParentheses += 1;
            }
        }
    }
    return openingParentheses + closingParentheses;
}