from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        ans = {}
        for i in arr:
            if i not in ans:
                ans[i] = 0
            ans[i] += 1
        return max(ans, key= ans.get)