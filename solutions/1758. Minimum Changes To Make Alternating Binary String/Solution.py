class Solution:
    def minOperations(self, st: str) -> int:
        s = list(st)
        n = len(s)
        count = 0
        for i in range(n - 1):
            if s[i] == s[i+1]:
                s[i+1] = '1' if s[i+1] == '0' else '0'
                count+=1
        return min(count, n - count)