# solutions\1287. Element Appearing More Than 25% In Sorted Array

Difficulty: `easy`

Topics: `Array`

## Q

Given an integer array **sorted** in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

Example 1:

```
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
```

Example 2:

```
Input: arr = [1,1]
Output: 1
```

Constraints:

- 1 <= `arr.length` <= 10<sup>4</sup>
- 0 <= `arr[i]` <= 10<sup>5</sup>

## S

### Python

#### Solution 1

```python
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        ans = {}
        for i in arr:
            if i not in ans:
                ans[i] = 0
            ans[i] += 1
        return max(ans, key= ans.get)
```

#### Solution 2

```python
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        for i, val in enumerate(arr):
            if val == arr[i + (n >> 2)]:
                return val
        return 0
```
