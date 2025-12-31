# Note

- Note that each senator should ban the closet senator of the opposite party. In this sense, this is a greedy algorithm.

- One idea is to use a single queue. Then, the senator at the start of the queue takes action and goes to the end of the queue. Here, the cost of each ban is $\mathsf{O}(k)$, where $k$ is the length of queue. This is because we remove a middle element from the queue. Consequently, the time complexity is $\mathsf{O}(n^2)$, where $n$ is the number of senators. For example, consider the senate `DDDDDRRRRR`.

- Another idea is to use two queues and store the indices of the Dire and Radiant senators in each queque. On each turn, we look to the beginning of the queues, the senator with smaller index can take action and then goes to the end of the queue with a shifted index by $n$, which is the size of the senate. Here, we do not remove any element from the middle of a queue. We only enque and deque, which is what the queues are designed for. This has time complexity $\mathsf{O}(n)$.
