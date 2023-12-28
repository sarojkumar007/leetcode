# solutions\1531. String Compression II

Difficulty: `hard`

Topics: `String`, `Dynamic Programming`

## Q

[Run-length encoding](http://en.wikipedia.org/wiki/Run-length_encoding) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string `"aabccc"` we replace `"aa"` by `"a2"` and replace `"ccc"` by `"c3"`. Thus the compressed string becomes `"a2bc3"`.

Notice that in this problem, we are not adding `'1'` after single characters.

Given a string `s` and an integer `k`. You need to delete at most `k` characters from `s` such that the run-length encoded version of `s` has minimum length.

Find _the minimum length of the run-length encoded version of `s` after deleting at most `k` characters_.

<br>

Example 1:

```
Input: s = "aaabcccd", k = 2
Output: 4
Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.
```

Example 2:

```
Input: s = "aabbaa", k = 2
Output: 2
Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.
```

Example 3:

```
Input: s = "aaaaaaaaaaa", k = 0
Output: 3
Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.
```

Constraints:

- `1 <= s.length <= 100`
- `0 <= k <= s.length`
- `s` contains only lowercase English letters.

## S

### Python

```python
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        cache = {}

        # O(n^2*k)
        def count(i,k,prev,prev_cnt):
            if (i,k,prev,prev_cnt) in cache:
                return cache[(i,k,prev,prev_cnt)]

            if k < 0: # Needs revision
                return float('inf')

            if i == len(s):
                return 0

            if s[i] == prev: # same
                incr = 1 if prev_cnt in [1,9,99] else 0
                res = incr + count(i+1,k,prev,prev_cnt+1)
            else: # different than prev
                res = min(
                    count(i+1,k-1,prev,prev_cnt), # delete
                    1 + count(i+1,k,s[i],1) # don't delete
                )

            cache[(i,k,prev,prev_cnt)] = res
            return res


        return count(0,k,"",0)
```
