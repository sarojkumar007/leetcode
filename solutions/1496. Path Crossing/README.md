# solutions\1496. Path Crossing

Difficulty: `easy`

Topics: `Hash Table`, `String`

## Q

Given a string `path`, where `path[i] = 'N'`, `'S'`, `'E'` or `'W'`, each representing moving one unit north, south, east, or west, respectively. You start at the origin `(0, 0)` on a 2D plane and walk on the path specified by `path`.

Return _true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited_.
<br>Return _false_ otherwise.

Example 1:

![Ex1](https://assets.leetcode.com/uploads/2020/06/10/screen-shot-2020-06-10-at-123929-pm.png)

```
Input: path = "NES"
Output: false
Explanation: Notice that the path doesn't cross any point more than once.
```

Example 2:

![Ex2](https://assets.leetcode.com/uploads/2020/06/10/screen-shot-2020-06-10-at-123843-pm.png)

```
Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
```

Constraints:

- `1 <= path.length <= 10`<sup>`4`</sup>
- `path[i]` is either `'N'`, `'S'`, `'E'`, or `'W'`.

## S

### Python

```python
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        paths = [[0,0]]
        point = [0,0]
        for d in path:
            match d:
                case 'N':
                    point[1] += 1
                case 'S':
                    point[1] -= 1
                case 'E':
                    point[0] += 1
                case _:
                    point[0] -= 1
            if point in paths:
                return True
            else:
                paths.append(point[:])
```

### TypeScript

```ts
function isPathCrossing(path: string): boolean {
  let [x, y] = [0, 0];
  const paths: Set<number> = new Set();
  // Starting Point
  paths.add(0);
  for (const d of path) {
    if (d === "N") y++;
    else if (d === "S") y--;
    else if (d === "E") x++;
    else if (d === "W") x--;

    const point = x * 20000 + y; // 20000 Constraint OR any High No
    if (paths.has(point)) return true;
    paths.add(point);
  }
  return false;
}
```
