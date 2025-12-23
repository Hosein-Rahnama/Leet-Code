# Note

- The main step in Dynamic Programming (DP) solutions is to understand the recursive pattern in the problem. This is actually the main line of thought in Divide and Conquer (DC) algorithms. The main difference is that the DP solution implements the recursive relation effectively by using a memorization or bottom-up approach.

- In this problem, `min_cost[i]` is the cost of *reaching* stair `i`. Consequetly, for leaving that stair you have to pay `cost[i]`. Consider an artificial stair after the last one. Then, reaching the top floor is equivalent to reaching this artificial stair. Now, the recursive relation should be easy to understand.
