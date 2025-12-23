# Note

- The trivial solution is to consider a moving window of length $k$ and compute the average of values within this window at each iteration. This has time complexity of $\mathsf{O}(n k)$. However, if you update the averages recursively, this becomes $\mathsf{O}(n)$.
