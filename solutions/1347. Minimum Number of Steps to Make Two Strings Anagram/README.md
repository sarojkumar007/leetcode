# solutions\1347. Minimum Number of Steps to Make Two Strings Anagram

Difficulty: `medium`

Topics: `Hash Table`, `String`, `Counting`

## Q

You are given two strings of the same length `s` and `t`. In one step you can choose **any character** of `t` and replace it with **another character**.

Return _the minimum number of steps to make `t` an anagram of `s`_.

An **Anagram** of a string is a string that contains the same characters with a different (or the same) ordering.

<br>

Example 1:

```
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
```

Example 2:

```
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
```

Example 3:

```
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams.
```

Constraints:

- `1 <= s.length <= 5 * 10`<sup>`4`</sup>
- `s.length == t.length`
- `s` and `t` consist of lowercase English letters only.

## S

### Python

```python
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt = Counter(s)
        ans = 0
        for c in t:
            if cnt[c] > 0:
                cnt[c] -= 1
            else:
                ans += 1
        return ans
```
