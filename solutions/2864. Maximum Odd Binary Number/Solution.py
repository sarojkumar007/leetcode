from collections import Counter


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = Counter(s)
        res = ['1'] * (cnt['1'] - 1 if cnt['1'] > 0 else 0) + ['0'] * cnt['0'] + ['1']
        return ''.join(res)