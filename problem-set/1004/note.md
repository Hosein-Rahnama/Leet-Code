# Note

- The problem can be restated as finding the longest subarray with at most $k$ zeros.

- We make a sliding window that changes size based on the number of zeros within the window. If the number of zeros is less than $k$, we expand the window. On the other hand, if the number of zeros in the window is greater than $k$, we shrink the window.
