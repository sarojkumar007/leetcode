# solutions\1578. Minimum Time to Make Rope Colorful

Difficulty: `medium`

Topics: `Array`, `String`, `Dynamic Programming`, `Greedy`

## Q

Alice has `n` balloons arranged on a rope. You are given a **0-indexed** string colors where `colors[i]` is the color of the `i`<sup>`th`</sup> balloon.

Alice wants the rope to be colorful. She does not want **two consecutive balloons** to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it **colorful**. You are given a **0-indexed** integer array `neededTime` where `neededTime[i]` is the time (in seconds) that Bob needs to remove the `i`<sup>`th`</sup> balloon from the rope.

Return _the **minimum time** Bob needs to make the rope colorful_.

Example 1:

![Ex1](https://assets.leetcode.com/uploads/2021/12/13/ballon1.jpg)

```
Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.
```

Example 2:

![Ex2](https://assets.leetcode.com/uploads/2021/12/13/balloon2.jpg)

```
Input: colors = "abc", neededTime = [1,2,3]
Output: 0
Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.
```

Example 3:

![Ex3](https://assets.leetcode.com/uploads/2021/12/13/balloon3.jpg)

```
Input: colors = "aabaa", neededTime = [1,2,3,4,1]
Output: 2
Explanation: Bob will remove the ballons at indices 0 and 4. Each ballon takes 1 second to remove.
There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.
```

Constraints:

- `n == colors.length == neededTime.length`
- `1 <= n <= 10`<sup>`5`</sup>
- `1 <= neededTime[i] <= 10`<sup>`4`</sup>
- `colors` contains only lowercase English letters.

## S

### Python

```python
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = i = 0
        n = len(colors)
        while i < n:
            j = i
            s = mx = 0
            while j < n and colors[j] == colors[i]:
                s += neededTime[j]
                if mx < neededTime[j]:
                    mx = neededTime[j]
                j += 1
            if j - i > 1:
                ans += s - mx
            i = j
        return ans
```
