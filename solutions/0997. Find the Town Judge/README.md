# solutions\0997. Find the Town Judge

Difficulty: `easy`

Topics: `Array`, `Hash Table`, `Graph`

## Q

In a town, there are n people labeled from `1` to `n`. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

- The town judge trusts nobody.

- Everybody (except for the town judge) trusts the town judge.

- There is exactly one person that satisfies properties 1 and 2.

You are given an array `trust` where `trust[i] = [a`<sub>`i`</sub>`, b`<sub>`i`</sub>`]` representing that the person labeled `a`<sub>`i`</sub> trusts the person labeled `b`<sub>`i`</sub>. If a trust relationship does not exist in `trust` array, then such a trust relationship does not exist.

Return _the label of the town judge if the town judge exists and can be identified, or return `-1` otherwise_.

<br>

Example 1:

```
Input: n = 2, trust = [[1,2]]
Output: 2
```

Example 2:

```
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
```

Example 3:

```
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
```

Constraints:

- `1 <= n <= 1000`
- `0 <= trust.length <= 10`<sup>`4`</sup>
- `trust[i].length == 2`
- All the pairs of `trust` are **unique**.
- `a`<sub>`i`</sub>` != b`<sub>`i`</sub>
- `1 <= a`<sub>`i`</sub>`, b`<sub>`i`</sub>` <= n`

## S

### Python

```python
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        cnt1 = [0] * (n + 1)
        cnt2 = [0] * (n + 1)
        for a, b in trust:
            cnt1[a] += 1
            cnt2[b] += 1
        for i in range(1, n + 1):
            if cnt1[i] == 0 and cnt2[i] == n - 1:
                return i
        return -1
```
