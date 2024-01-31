from typing import List


class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        s = [] # [temp,index]

        for i,t in enumerate(temps):
            while s and t > s[-1][0]:
                sTemp, sIdx = s.pop()
                res[sIdx] = i - sIdx
            s.append([t,i])
        
        return res