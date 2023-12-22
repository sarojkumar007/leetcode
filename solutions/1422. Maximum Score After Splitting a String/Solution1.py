class Solution:
    def maxScore(self, s: str) -> int:
        # Precomputed 1s + first 0, if any
        ans = score = (s[0] == '0') + s[1:].count('1')

        # iterate from 1 to (len - 1)
        # EACH ITERATION, if 0, score inceases, if 1,score decreases as it was pre-computed.
        # with each iteration, check the max score.

        for i in range(1,len(s)-1):
            if s[i] == '0':
                score += 1
            else:
                score -= 1
            ans = max(ans,score)
        return ans
