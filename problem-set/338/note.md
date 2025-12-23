# Note

- The trivial solution for this problem is to loop over numbers from $0$ to $n$. Then, in each loop we convert the number to its binary string and count the number of $1$ bits. For a number $i$, the length of its binary string is of order $\mathsf{O}(\log(i))$. Summing over $i$, we conclude that the time complexity of this solution is $\mathsf{O}(n \log(n))$.


- We can improve the time complexity to $\mathsf{O}(n)$ by compting the number of $1$ bits recursively. The recursive relation governing this problem is a little tricky. Suppose that $f: \mathbb{N} \to \mathbb{N}$ is a function that takes a natural number and returns the number of $1$s in its binary representation. If $n$ is even, then $$f(n) = f(n/2),$$ since binary representation of $n$ is a left shift of that of $n/2$. On the other side, if $n$ is odd, then $$f(n) = f(n - 1) + 1,$$ since the right most bit in binary representation of $n - 1$ is $0$. Moreover, binary representation of $n - 1$ has the same number of $1$ bits as that of $(n - 1)/2$. Combining these cases, we arrive at $$f(n) = f(\lfloor n/2 \rfloor) + (n\,\, \mathrm{mod}\,\, 2).$$
