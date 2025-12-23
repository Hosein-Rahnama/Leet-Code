# Note

- If division was allowed, you could compute the product of all elements of the array. Then, on a signle pass over the array, you could divide this quantity by each element. However, this requires handling of arrays containing zeros in separate cases. If there is one zero in the array, the only non-zero element in the product array will correspond to that element. If there are more than one zero, the product array will be all zeros.

- The key to the solution without using divison is to recursively compute the prefix and suffix products on a single pass. Then, you can easily compute the product from them.

- Both solutions have $\mathsf{O}(n)$ time complexity. However, the first one has $\mathsf{O}(1)$ space complexity, while the second one has $\mathsf{O}(n)$ space complexity.
