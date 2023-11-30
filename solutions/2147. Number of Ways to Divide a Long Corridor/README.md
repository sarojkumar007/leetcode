# solutions\2147. Number of Ways to Divide a Long Corridor

Difficuly: `hard`

Topics: `Math`, `String`, `Dynamic Programming`

## Q

Along a long library corridor, there is a line of seats and decorative plants. You are given a 0-indexed string corridor of length n consisting of letters 'S' and 'P' where each 'S' represents a seat and each 'P' represents a plant.

One room divider has already been installed to the left of index 0, and another to the right of index n - 1. Additional room dividers can be installed. For each position between indices i - 1 and i (1 <= i <= n - 1), at most one divider can be installed.

Divide the corridor into non-overlapping sections, where each section has exactly two seats with any number of plants. There may be multiple ways to perform the division. Two ways are different if there is a position with a room divider installed in the first way but not in the second way.

Return the number of ways to divide the corridor. Since the answer may be very large, return it modulo 10<sup>9</sup> + 7. If there is no way, return 0.

Example 1:

![Ex1](https://assets.leetcode.com/uploads/2021/12/04/1.png)

Input: corridor = "SSPPSPS" <br>
Output: 3 <br>
Explanation: There are 3 different ways to divide the corridor.
The black bars in the above image indicate the two room dividers already installed.
Note that in each of the ways, each section has exactly two seats.

Example 2:

![Ex2](https://assets.leetcode.com/uploads/2021/12/04/2.png)

Input: corridor = "PPSPSP" <br>
Output: 1 <br>
Explanation: There is only 1 way to divide the corridor, by not installing any additional dividers. <br>
Installing any would create some section that does not have exactly two seats.

Example 3:

![Ex3](https://assets.leetcode.com/uploads/2021/12/12/3.png)

Input: corridor = "S" <br>
Output: 0 <br>
Explanation: There is no way to divide the corridor because there will always be a section that does not have exactly two seats.

Constraints:

- n == corridor.length
- 1 <= n <= 10<sup>5</sup>
- corridor[i] is either 'S' or 'P'.

## S

### Python

```python
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        @cache
        def dfs(i, cnt):
            if i == n:
                return int(cnt == 2)
            cnt += corridor[i] == 'S'
            if cnt > 2:
                return 0
            ans = dfs(i + 1, cnt)
            if cnt == 2:
                ans += dfs(i + 1, 0)
                ans %= mod
            return ans

        n = len(corridor)
        mod = 10**9 + 7
        ans = dfs(0, 0)
        dfs.cache_clear()
        return ans
```
