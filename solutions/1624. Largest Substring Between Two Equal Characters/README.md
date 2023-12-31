# solutions\1624. Largest Substring Between Two Equal Characters

Difficulty: `easy`

Topics: `Hash Table`, `String`

## Q

Given a string `s`, return _the length of the longest substring between two equal characters, excluding the two characters_. If there is no such substring return `-1`.

A **substring** is a contiguous sequence of characters within a string.

<br>

Example 1:

```
Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
```

Example 2:

```
Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".
```

Example 3:

```
Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
```

Constraints:

- `1 <= s.length <= 300`
- `s` contains only lowercase English letters.

## S

### Python

```python
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        ans = -1
        for i, c in enumerate(s):
            if c in d:
                ans = max(ans, i - d[c] - 1)
            else:
                d[c] = i
        return ans
```

### TypeScript

```typescript
function maxLengthBetweenEqualCharacters(s: string): number {
  const n = s.length;
  const pos = new Array(26).fill(-1);
  let res = -1;
  for (let i = 0; i < n; i++) {
    const j = s[i].charCodeAt(0) - "a".charCodeAt(0);
    if (pos[j] === -1) {
      pos[j] = i;
    } else {
      res = Math.max(res, i - pos[j] - 1);
    }
  }
  return res;
}
```
