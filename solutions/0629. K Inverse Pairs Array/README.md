# solutions\0629. K Inverse Pairs Array

Difficulty: `hard`

Topics: `Dynamic Programming`

## Q

For an integer array `nums`, an **inverse pair** is a pair of integers `[i, j]` where `0 <= i < j < nums.length` and `nums[i] > nums[j]`.

Given two integers `n` and `k`, return _the number of different arrays consist of numbers from `1` to `n` such that there are exactly `k` **inverse pairs**_. Since the answer can be huge, return it **modulo** `10`<sup>`9`</sup>` + 7`.

<br>

Example 1:

```
Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
```

Example 2:

```
Input: n = 3, k = 1
Output: 2
Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
```

Constraints:

- `1 <= n <= 1000`
- `0 <= k <= 1000`

## S

### Python

```python
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        prev = [0] * (k + 1)
        prev[0] = 1

        for N in range(1, n + 1):
            curr = [0] * (k + 1)
            total = 0

            for K in range(k + 1):
                if K >= N:
                    total -= prev[K - N]
                total = (total + prev[K]) % MOD
                curr[K] = total
            prev = curr
        return prev[K]
```
