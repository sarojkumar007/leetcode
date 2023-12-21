from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[0])
        max_distance = 0
        n = len(points)
        for x in range(n-1):
            dist = points[x+1][0] - points[x][0]
            if(dist > max_distance):
                max_distance = dist
        return max_distance