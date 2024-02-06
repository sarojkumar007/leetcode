# solutions\0387. First Unique Character in a String

Difficulty: `easy`

Topics: `Hash Table`, `String`, `Queue`, `Counting`

## Q

Given a string `s`, _find the first non-repeating character in it and return its index_. If it does not exist, return `-1`.

<br>

Example 1:

```
Input: s = "leetcode"
Output: 0
```

Example 2:

```
Input: s = "loveleetcode"
Output: 2
```

Example 3:

```
Input: s = "aabb"
Output: -1
```

Constraints:

- `1 <= s.length <= 10`<sup>`5`</sup>
- `s` consists of only lowercase English letters.

## S

### Python

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1
```
