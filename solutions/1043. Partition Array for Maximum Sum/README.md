# solutions\1043. Partition Array for Maximum Sum

Difficulty: `medium`

Topics: `Array`, `Dynamic Programming`

## Q

Given an integer array `arr`, partition the array into (contiguous) subarrays of length **at most** `k`. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return _the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a **32-bit** integer_.

<br>

Example 1:

```
Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
```

Example 2:

```
Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
```

Example 3:

```
Input: arr = [1], k = 1
Output: 1
```

Constraints:

- `1 <= arr.length <= 500`
- `0 <= arr[i] <= 10`<sup>`9`</sup>
- `1 <= k <= arr.length`

## S

### Python

```python
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * k
        dp[0] = arr[0]

        for i in range(1, n):
            curr_max = 0
            max_at_i = 0
            for j in range(i, i - k, -1):
                if j < 0:
                    break
                curr_max = max(curr_max, arr[j])
                window_size = i - j + 1
                curr_sum = window_size * curr_max

                sub_sum = dp[(j - 1) % k] if j > 0 else dp[-1]
                max_at_i = max(max_at_i, sub_sum + curr_sum)

            dp[i % k] = max_at_i

        return dp[(n - 1) % k]
```
