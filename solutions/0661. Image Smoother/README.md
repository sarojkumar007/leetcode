# solutions\0661. Image Smoother

Difficulty: `easy`

Topics: `Array`, `Matrix`

## Q

An **image smoother** is a filter of the size `3 x 3` that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).

![Diagram](https://assets.leetcode.com/uploads/2021/05/03/smoother-grid.jpg)

Given an` m x n` integer matrix `img` representing the grayscale of an image, return _the image after applying the smoother on each cell of it_.

<br>

Example 1:

![Ex1](https://assets.leetcode.com/uploads/2021/05/03/smooth-grid.jpg)

```
Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
```

Example 2:

![Ex2](https://assets.leetcode.com/uploads/2021/05/03/smooth2-grid.jpg)

```
Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
```

Constraints:

- `m == img.length`
- `n == img[i].length`
- `1 <= m, n <= 200`
- `0 <= img[i][j] <= 255`

## S

### Python

```python
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                s = cnt = 0
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < m and 0 <= y < n:
                            cnt += 1
                            s += img[x][y]
                ans[i][j] = s // cnt
        return ans
```

### TypeScript

```ts
function imageSmoother(img: number[][]): number[][] {
  const m = img.length;
  const n = img[0].length;
  const locations = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 0],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
  ];

  const res: number[][] = [];
  for (let i = 0; i < m; i++) {
    res.push([]);
    for (let j = 0; j < n; j++) {
      let sum = 0;
      let count = 0;
      for (const [y, x] of locations) {
        if ((img[i + y] || [])[j + x] != null) {
          sum += img[i + y][j + x];
          count++;
        }
      }
      res[i].push(Math.floor(sum / count));
    }
  }
  return res;
}
```
