# Note

- The exhaustive search solution for this problem goes over all triplets and checks the increasing condition. It has $\mathsf{O}(n^3)$ time complexity with $\mathsf{O}(1)$ space complexity.

- In another solution, you can compute the minimum of the prefix array and maximum of suffix array on single passes. Then, you can easily check the increasing condition on another pass. This has time complexity of $\mathsf{O}(n)$ and space complexity of $\mathsf{O}(n)$.

- You can improve the space complexity of the previous solution to $\mathsf{O}(1)$ by using the Longest Increasing Subsequence(LIS) algorithm.
