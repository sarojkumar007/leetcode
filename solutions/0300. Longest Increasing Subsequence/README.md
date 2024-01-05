# solutions\0300. Longest Increasing Subsequence

Difficulty: `medium`

Topics: `Array`, `Binary Search`, `Dynamic Programming`

## Q

Given an integer array `nums`, return _the length of the longest **strictly increasing
<a title="A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.">subsequence</a>**_.

<br>

Example 1:

```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

Example 2:

```
Input: nums = [0,1,0,3,2,3]
Output: 4
```

Example 3:

```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

Constraints:

- `1 <= nums.length <= 2500`
- `-10`<sup>`4`</sup>` <= nums[i] <= 10`<sup>`4`</sup>

**Follow up:** Can you come up with an algorithm that runs in `O(n log(n))` time complexity?

## S

### Python

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        LIS = [1] * n

        for i in range(n -1, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)
```
