# Note

- There are two different approaches to this problem. The first one is to calculate the transpose and compare row by row. This has time complexity of $\mathsf{O}(n^3)$. Another solution is store the rows and columns as the keys of a hash table and count the number of their appearance. Then, we simply multiply the row and column frequencies and sum them up. This has expected time complexity $\mathsf{O}(n^2)$.
