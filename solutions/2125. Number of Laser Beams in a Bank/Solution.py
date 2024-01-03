from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = bank[0].count('1')
        ans = 0

        for i in range(1,len(bank)):
            curr = bank[i].count('1')

            if curr:
                ans += (prev * curr)
                prev = curr
        
        return ans