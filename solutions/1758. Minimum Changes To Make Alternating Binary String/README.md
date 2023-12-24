# solutions\1758. Minimum Changes To Make Alternating Binary String

Difficulty: `easy`

Topics: `String`

## Q

You are given a string `s` consisting only of the characters `'0'` and `'1'`. In one operation, you can change any `'0'` to `'1'` or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string `"010"` is alternating, while the string `"0100"` is not.

Return _the **minimum** number of operations needed to make s alternating_.

<br>

Example 1:

```
Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.
```

Example 2:

```
Input: s = "10"
Output: 0
Explanation: s is already alternating.
```

Example 3:

```
Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".
```

Constraints:

- `1 <= s.length <= 10`<sup>`4`</sup>
- `s[i]` is either `'0'` or `'1'`.

## S

### Python

```python
class Solution:
    def minOperations(self, st: str) -> int:
        s = list(st)
        n = len(s)
        count = 0
        for i in range(n - 1):
            if s[i] == s[i+1]:
                s[i+1] = '1' if s[i+1] == '0' else '0'
                count+=1
        return min(count, n - count)
```

### TypeScript

```typescript
function minOperations(s: string): number {
  const n = s.length;
  const sArr: string[] = s.split("");
  let count: number = 0;
  for (let i = 0; i < n; i++) {
    if (sArr[i] === sArr[i + 1]) {
      // sArr[i + 1] = sArr[i + 1] === "0" ? "1" : "0";
      sArr[i + 1] = (1 - +sArr[i + 1]).toString();
      count++;
    }
  }
  return Math.min(count, n - count);
}
```
