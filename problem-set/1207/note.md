# Note

- Without using hash tables, one can sort the array to easily count the number of occurrences and store them into another array. Now, you sort this new array and check if any of its adjacent elements are similar. This solution has $\mathsf{O}(n \log(n))$ time complexity and $\mathsf{O}(n)$ space complexity.

- Using a hash table, we store the number of occurrences. Then, we compare the length of the list of these values with the length of the corresponding set. This solution has $\mathsf{O}(n)$ expected time complexity and $\mathsf{O}(n)$ space complexity.
