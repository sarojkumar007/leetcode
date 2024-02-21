# solutions\0201. Bitwise AND of Numbers Range

Difficulty: `medium`

Topics: `Bit Manipulation`

## Q

Given two integers `left` and `right` that represent the range `[left, right]`, return _the bitwise AND of all numbers in this range, inclusive_.

<br>

Example 1:

```
Input: left = 5, right = 7
Output: 4
```

Example 2:

```
Input: left = 0, right = 0
Output: 0
```

Example 3:

```
Input: left = 1, right = 2147483647
Output: 0
```

Constraints:

- `0 <= left <= right <= 2`<sup>`31`</sup>` - 1`

## S

### Python

```python
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= right - 1
        return right
```
