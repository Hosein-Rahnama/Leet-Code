# 933. Number of Recent Calls

from typing import List


class Solution:
    def get_recent_calls(self, calls: List[int]) -> List[int]:
        num_recent_calls = []
        cnt = RecentCounter()
        for t in calls:
            num_recent_calls.append(cnt.ping(t))
        return num_recent_calls


class RecentCounter:
    def __init__(self):
        self.counter = 0
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < (t - 3000):
            self.requests.pop(0)
        num = len(self.requests)
        return num
