# solutions\935. Knight Dialer

Difficuly: `medium`

Topics: `Dynamic Programming`

## Q

The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

A chess knight can move as indicated in the chess diagram below:

![Diagram](https://assets.leetcode.com/uploads/2020/08/18/chess.jpg)

We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).

![D2](https://assets.leetcode.com/uploads/2020/08/18/phone.jpg)

Given an integer n, return how many distinct phone numbers of length n we can dial.

You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo 10<sup>9</sup> + 7.

Example 1:

Input: n = 1 <br>
Output: 10 <br>
Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.

Example 2:

Input: n = 2 <br>
Output: 20 <br>
Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]

Example 3:

Input: n = 3131 <br>
Output: 136006598 <br>
Explanation: Please take care of the mod.

Constraints:

- 1 <= n <= 5000

## S

### Python

```python
class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        f = [1] * 10
        for _ in range(n - 1):
            t = [0] * 10
            t[0] = f[4] + f[6]
            t[1] = f[6] + f[8]
            t[2] = f[7] + f[9]
            t[3] = f[4] + f[8]
            t[4] = f[0] + f[3] + f[9]
            t[6] = f[0] + f[1] + f[7]
            t[7] = f[2] + f[6]
            t[8] = f[1] + f[3]
            t[9] = f[2] + f[4]
            f = t
        return sum(t) % (10**9 + 7)
```
