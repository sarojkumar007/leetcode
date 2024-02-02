from collections import deque
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        queue = deque(range(0,10))
        while queue:
            n = queue.popleft()
            if n > high:
                continue
            if low <= n <= high and n not in res:
                res.append(n)
            last_digit = n%10
            if last_digit < 9:
                queue.append(n*10 + (last_digit+1))
        return res