# solutions\1637. Widest Vertical Area Between Two Points Containing No Points

Difficulty: `medium`

Topics: `Array`, `Sorting`

## Q

Given `n` `points` on a 2D plane where `points[i] = [x`<sub>`i`</sub>`, y`<sub>`i`</sub>`]`, Return _the **widest vertical area** between two points such that no points are inside the area_.

A **vertical area** is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The **widest vertical area** is the one with the maximum width.

Note that points **on the edge** of a vertical area **are not** considered included in the area.

Example 1:

![Ex1](https://assets.leetcode.com/uploads/2020/09/19/points3.png)

```​
Input: points = [[8,7],[9,9],[7,4],[9,7]]
Output: 1
Explanation: Both the red and the blue area are optimal.
```

Example 2:

```
Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
Output: 3
```

Constraints:

- `n == points.length`
- `2 <= n <= 10`<sup>`5`</sup>
- `points[i].length == 2`
- `0 <= x`<sub>`i`</sub>`, y`<sub>`i`</sub>` <= 10`<sup>`9`</sup>

## S

### Python

#### Solution 1

```python
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
```

#### Solution 2

```python
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        return max(b[0] - a[0] for a, b in pairwise(points))
```

### TypeScript

```ts
function maxWidthOfVerticalArea(points: number[][]): number {
  points.sort((a, b) => a[0] - b[0]);
  let max_dist = 0;
  for (let i = 0; i < points.length - 1; i++) {
    const dist = points[i + 1][0] - points[i][0];
    if (max_dist < dist) max_dist = dist;
  }
  return max_dist;
}
```
