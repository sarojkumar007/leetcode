class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        ans = ""
        for i in range(max(n1,n2)):
            if i < n1:
                ans += word1[i]
            if i < n2:
                ans += word2[i]
        return ans
