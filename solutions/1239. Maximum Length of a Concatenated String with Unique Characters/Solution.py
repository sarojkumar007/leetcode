from collections import Counter
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charSet = set()

        def overlap(charSet,s):
            c = Counter(charSet) + Counter(s)
            return max(c.values()) > 1 # if any char is duplicate
        
        def backtrack(i):
            if i == len(arr):
                return len(charSet)
            
            res = 0
            if not overlap(charSet, arr[i]):
                for c in arr[i]:
                    charSet.add(c)
                res = backtrack(i+1)
                # Cleanup for Next Backtrack at line 22
                for c in arr[i]:
                    charSet.remove(c)

            return max(res, backtrack(i+1))
        
        return backtrack(0)