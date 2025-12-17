from collections import deque


class RecentCounter:
    def __init__(self):
        self.counter = 0
        self.requests = deque([])

    def ping(self, t: int) -> int:
        requests = self.requests
        requests.append(t)
        while requests[0] < (t - 3000):
            requests.popleft()
        num = len(requests)
        return num
