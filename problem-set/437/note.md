# Note

- The difficulty of this problem lies in the fact the paths do not necessarily start from the root. Actually, if the we consider all paths that start from the root with a desired target sum, we can write a simple recursive relation to count these paths. However, no such recurrence can be obtained for paths that does not start from the root.

- One easy solution is to have a function which counts the paths starting from the root with the desired target sum by using a recurrence relation. Then, you can loop over all the nodes and call that function and sum the results. Looping over the nodes can be done via BFS or DFS.

- Another solution is to memorize the sums of all downward paths up to the current node. Then, you loop over all the nodes, and ask if there is a downward path ending at this node with the desired target sum. In this solution, our calculation at node $i$ is $\mathsf{O}(h_i)$, where $h_i$ is the height of that node. This solution has space complexity $\mathsf{O}(h)$, where $h$ is the height of the tree.

- One can also memorize sums of all paths from the root to the current node with their number of occurence in a hash table. Then, you loop over all the nodes, and see if you have seen a rooted path whose sum equals the `target_sum - current_sum`. This shows if there is a downward path with the desired sum, ending at this node or not. In this solution, our expected calculation at each node is $\mathsf{O}(1)$. This solution has space complexity $\mathsf{O}(n)$, where $n$ is the number of nodes.
