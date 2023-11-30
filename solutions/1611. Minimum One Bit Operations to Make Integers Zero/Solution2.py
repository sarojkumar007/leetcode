class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        string = str(bin(n))
        ans = 0
        lastbit = 0
        for i, bit in enumerate(string[2:]):
            if bit == '1':
                x = 0 if lastbit else 1
            else:
                x = 1 if lastbit else 0
            ans = (ans << 1) | x 
            lastbit = x
        return ans