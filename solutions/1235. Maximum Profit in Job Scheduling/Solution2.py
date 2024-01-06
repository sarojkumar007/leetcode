import bisect
from typing import List


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]
            
            # CASE: don't include
            res = dfs(i+1)

            # CASE: include
            j = bisect.bisect(intervals,(intervals[i][1],-1,-1)) # binary search next StartTime, based on current endTime
            cache[i] = res = max(res,intervals[i][2]+ dfs(j)) # max of curr profit + profit of j(next startTime)
            return res
        
        return dfs(0)