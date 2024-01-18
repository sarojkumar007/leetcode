# solutions\0070. Climbing Stairs

Difficulty: `easy`

Topics: `Math`, `Dynamic Programming`, `Memoization`

## Q

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

<br>

Example 1:

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

Example 2:

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

Constraints:

- `1 <= n <= 45`

## S

### Python

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        # DP with Tree DFS, We can use cache,
        # THEN we move to the solution for Fibonacci

        first, second = 1,1

        for i in range(n-1):
            first, second = first+second, first
        return first
```

### TypeScript

```typescript
function climbStairs(n: number): number {
  let first = 1,
    second = 1;

  for (let i = 0; i < n - 1; i++) {
    const temp = first;
    first += second;
    second = temp;
  }
  return first;
}
```
