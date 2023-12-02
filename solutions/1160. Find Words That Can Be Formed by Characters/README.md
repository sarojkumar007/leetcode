# solutions\1160. Find Words That Can Be Formed by Characters

Difficulty: `easy`

Topics: `Array`, `Hash Table`, `String`

## Q

You are given an array of strings `words` and a string `chars`.

A string is **good** if it can be formed by characters from chars (each character can only be used once).

_Return the sum of lengths of all good strings in words._

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach" <br>
Output: 6 <br>
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr" <br>
Output: 10 <br>
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

Constraints:

- 1 <= words.length <= 1000
- 1 <= words[i].length, chars.length <= 100
- words[i] and chars consist of lowercase English letters.

## S

### Python

```python
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = Counter(chars)
        ans = 0
        for w in words:
            wc = Counter(w)
            if all(cnt[c] >= v for c, v in wc.items()):
                ans += len(w)
        return ans
```
