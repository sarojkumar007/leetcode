# solutions\0907. Sum of Subarray Minimums

Difficulty: `medium`

Topics: `Array`, `Dynamic Programming`, `Stack`, `Monotonic Stack`

## Q

Given an array of integers `arr`, find the sum of `min(b)`, where `b` ranges over every (contiguous) subarray of `arr`. Since the answer may be large, return _the answer **modulo** `10`<sup>`9`</sup>` + 7`_.

<br>

Example 1:

```
Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
```

Example 2:

```
Input: arr = [11,81,94,43,3]
Output: 444
```

Constraints:

- `1 <= arr.length <= 3 * 10`<sup>`4`</sup>
- `1 <= arr[i] <= 3 * 10`<sup>`4`</sup>

## S

### Python

```python
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        arr = [float('-inf')] + arr + [float("-inf")]
        stack = [] #(index, num)

        for i, n in enumerate(arr):
            while stack and n < stack[-1][1]:
                j, m = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j
                res = (res + m * left * right) % MOD
            stack.append((i,n))

        return res
```
