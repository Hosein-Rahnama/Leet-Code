# Note

- The trivial solution to this problem is to count number of occurences in one pass and store it in a hash table. This takes $\mathsf{O}(n)$ time complexity and $\mathsf{O}(n)$ space complexity.

- To improve the space complexity, we can take advantage of the algebraic properties of the exclusive OR operator, denoted by $\oplus$ . It is commutative and associative. Moreover, we have $a \oplus 0 = a$ and $a \oplus a = 0$. We compute $C = \oplus_{i = 0}^{n - 1}a_i$. Since all elements are repeated twice except one, we deduce that $C = a \oplus 0 = a$, where $a$ is that unique element.
