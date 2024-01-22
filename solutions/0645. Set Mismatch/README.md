# solutions\0645. Set Mismatch

Difficulty: `easy`

Topics: `Array`, `Hash Table`, `Bit Manipulation`, `Sorting`

## Q

You have a set of integers `s`, which originally contains all the numbers from `1` to `n`. Unfortunately, due to some error, one of the numbers in `s` got duplicated to another number in the set, which results in **repetition of one** number and **loss of another number**.

You are given an integer array `nums` representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return _them in the form of an array_.

<br>

Example 1:

```
Input: nums = [1,2,2,4]
Output: [2,3]
```

Example 2:

```
Input: nums = [1,1]
Output: [1,2]
```

Constraints:

- `2 <= nums.length <= 10`<sup>`4`</sup>
- `1 <= nums[i] <= 10`<sup>`4`</sup>

## S

### Python

#### Solution 1

```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0,0]
        n = len(nums)
        count = Counter(nums)

        for i in range(1,n+1):
            if count[i] == 0:
                res[1] = i
            if count[i] == 2:
                res[0] = i
        return res
```

#### Solution 2

```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0,0]

        for n in nums:
            n = abs(n)
            nums[n-1] = -nums[n-1]
            if nums[n-1] > 0:
                res[0] = n

        for i,n in enumerate(nums):
            if n > 0 and i+1 != res[0]:
                res[1] = i+1
                return res
```
