# Note

- The exhaustive search solution has $\mathsf{O}(n^2)$ time complexity.

- Another solution is to sort the array which takes $\mathsf{O}(n \log n)$ time complexity. Now, you set two pointers to the start and end of the array and move them toward the middle. This has $\mathsf{O}(1)$ space complexity.

- You can use a hash table to store the number of appearances of each number. Then, you can simply count the number of $k$-sum pairs. This solution has $\mathsf{O}(n)$ expected time complexity and $\mathsf{O}(n)$ space complexity.
