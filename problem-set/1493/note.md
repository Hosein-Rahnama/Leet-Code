# Note

- This is very similar to problem 1004. We find the longest subarray with at most $1$ zero and return its length minus one, since we have to delete one element. In this solution, the sliding window shrinks and expands based on the number of zeros within the window. 

- It is also possible to avoid shrinking the sliding window. In this strategy, we expand the window until we hit the maximum size possible so far. After that, we translate the window, while keeping track of the number of zeros within the window, denoted by $k$. In the sequel, if $k$ reduces, then there is an opportunity for expanding the window further.

- Pay attention to initial conditions for `num_zeros` in these two different solutions.
