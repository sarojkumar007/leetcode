# solutions\1291. Sequential Digits

Difficulty: `medium`

Topics: `Enumeration`

## Q

An integer has _sequential digits_ if and only if each digit in the number is one more than the previous digit.

Return a **sorted** list of all the integers in the range `[low, high]` inclusive that have sequential digits.

<br>

Example 1:

```
Input: low = 100, high = 300
Output: [123,234]
```

Example 2:

```
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
```

Constraints:

- `10 <= low <= high <= 10^9`

## S

### Python

```python
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        queue = deque(range(0,10))
        while queue:
            n = queue.popleft()
            if n > high:
                continue
            if low <= n <= high and n not in res:
                res.append(n)
            last_digit = n%10
            if last_digit < 9:
                queue.append(n*10 + (last_digit+1))
        return res
```

### TypeScript

```typescript
function sequentialDigits(low: number, high: number): number[] {
  const ans: number[] = [];
  for (let i = 1; i < 9; ++i) {
    let x = i;
    for (let j = i + 1; j < 10; ++j) {
      x = x * 10 + j;
      if (x >= low && x <= high) {
        ans.push(x);
      }
    }
  }
  ans.sort((a, b) => a - b);
  return ans;
}
```
