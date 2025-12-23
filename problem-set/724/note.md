# Note

- One can compute the left and right sums on one pass and store them in separate arrays. Then, one more pass determines the pivot index. This solution has $\mathsf{O}(n)$ time complexity and $\mathsf{O}(n)$ space complexity. However, recurive calculation of the left and right sums can improve the space complexity to $\mathsf{O}(1)$.
