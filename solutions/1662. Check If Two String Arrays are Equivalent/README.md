# solutions\1662. Check If Two String Arrays are Equivalent

Difficulty: `easy`

Topics: `Array`, `String`

## Q

Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"] <br>
Output: true <br>
Explanation: <br>
word1 represents string "ab" + "c" -> "abc" <br>
word2 represents string "a" + "bc" -> "abc" <br>
The strings are the same, so return true. <br>

Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"] <br>
Output: false <br>

Example 3:

Input: word1 = ["abc", "d", "defg"], word2 = ["abcddefg"] <br>
Output: true

Constraints:

- 1 <= word1.length, word2.length <= 10<sup>3</sup>
- 1 <= word1[i].length, word2[i].length <= 10<sup>3</sup>
- 1 <= sum(word1[i].length), sum(word2[i].length) <= 10<sup>3</sup>
- word1[i] and word2[i] consist of lowercase letters.

## S

### Python

#### Solution 1

```python
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
```

#### Solution 2

```python
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i = j = x = y = 0
        while i < len(word1) and j < len(word2):
            if word1[i][x] != word2[j][y]:
                return False
            x, y = x + 1, y + 1
            if x == len(word1[i]):
                x, i = 0, i + 1
            if y == len(word2[j]):
                y, j = 0, j + 1
        return i == len(word1) and j == len(word2)
```
