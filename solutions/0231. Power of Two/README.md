# solutions\0231. Power of Two

Difficulty: `easy`

Topics: `Math`, `Bit Manipulation`, `Recursion`

## Q

Given an integer `n`, return _`true` if it is a power of two. Otherwise, return `false`_.

An integer `n` is a power of two, if there exists an integer x such that n == 2x.

<br>

Example 1:

```
Input: n = 1
Output: true
Explanation: 20 = 1
```

Example 2:

```
Input: n = 16
Output: true
Explanation: 24 = 16
```

Example 3:

```
Input: n = 3
Output: false
```

Constraints:

- `-2`<sup>`31`</sup>` <= n <= 2`<sup>`31`</sup>` - 1`

## S

### Python

```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
```
