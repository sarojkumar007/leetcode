# solutions\2225. Find Players With Zero or One Losses

Difficulty: `medium`

Topics: `Array`, `Hash Table`, `Sorting`, `Counting`

## Q

You are given an integer array `matches` where `matches[i] = [winner`<sub>`i`</sub>`, loser`<sub>`i`</sub>`]` indicates that the player `winner`<sub>`i`</sub> defeated player `loser`<sub>`i`</sub> in a match.

Return a list `answer` of size `2` where:

- `answer[0]` is a list of all players that have **not** lost any matches.
- `answer[1]` is a list of all players that have lost exactly **one** match.

The values in the two lists should be returned in **increasing** order.

Note:

- You should only consider the players that have played **at least one** match.
- The testcases will be generated such that **no** two matches will have the **same** outcome.

<br>

Example 1:

```
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
```

Example 2:

```
Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].
```

Constraints:

- `1 <= matches.length <= 10`<sup>`5`</sup>
- `matches[i].length == 2`
- `1 <= winner`<sub>`i`</sub>`, loser`<sub>`i`</sub>` <= 10`<sup>`5`</sup>
- `winner`<sub>`i`</sub>` != loser`<sub>`i`</sub>
- All `matches[i]` are unique.

## S

### Python

```python
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        cnt = Counter()
        for a, b in matches:
            if a not in cnt:
                cnt[a] = 0
            cnt[b] += 1
        ans = [[], []]
        for u, v in cnt.items():
            if v < 2:
                ans[v].append(u)
        ans[0].sort()
        ans[1].sort()
        return ans
```
