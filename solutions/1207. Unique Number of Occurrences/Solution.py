from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        cnt_occurance = Counter(cnt.values())
        occ = list(cnt.values())
        return len(occ) == len(cnt_occurance.keys())