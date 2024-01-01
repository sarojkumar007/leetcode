# solutions\0455. Assign Cookies

Difficulty: `easy`

Topics: `Array`, `Two Pointers`, `Greedy`, `Sorting`

## Q

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child `i` has a greed factor `g[i]`, which is the minimum size of a cookie that the child will be content with; and each cookie `j` has a size `s[j]`. If `s[j] >= g[i]`, we can assign the cookie `j` to the child `i`, and the child `i` will be content. Your goal is to maximize the number of your content children and output the maximum number.

<br>

Example 1:

```
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
```

Example 2:

```
Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
You have 3 cookies and their sizes are big enough to gratify all of the children,
You need to output 2.
```

Constraints:

- `1 <= g.length <= 3 * 10`<sup>`4`</sup>
- `0 <= s.length <= 3 * 10`<sup>`4`</sup>
- `1 <= g[i], s[j] <= 2`<sup>`31`</sup>` - 1`

## S

### Python

```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cookie_index = 0
        for child_index, x in enumerate(g):
            while cookie_index < len(s) and s[cookie_index] < g[child_index]:
                cookie_index += 1
            if cookie_index >= len(s):
                return child_index
            cookie_index += 1
        return len(g)
```

### TypeScript

```typescript
function findContentChildren(g: number[], s: number[]): number {
  g.sort((a, b) => b - a); // Reverse
  s.sort((a, b) => b - a); // Reverse

  let count = 0;

  for (let i = 0; i < g.length; i++) {
    if (count >= s.length) break;
    else if (g[i] <= s[count]) count++;
  }
  return count;
}
```
