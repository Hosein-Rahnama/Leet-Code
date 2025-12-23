# Note

- The exhaustive search solution has $\mathsf{O}(n^2)$ time complexity.

- This can be improved to $\mathsf{O}(n)$ time complexity. The idea is to consider two pointers for the left and right walls. Then, we move the pointer to the shorter wall toward the middle while keeping track of the maximum capacity seen so far.
