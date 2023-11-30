# solutions\1611. Minimum One Bit Operations to Make Integers Zero

Difficuly: `hard`

Topics: `Dynamic Programming`, `Bit Manipulation`, `Memoization`

## Q

Given an integer `n`, you must transform it into 0 using the following operations any number of times:

Change the rightmost (0th) bit in the binary representation of n. <br>
Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0. <br>
Return the minimum number of operations to transform n into 0.

Example 1:

Input: n = 3 <br>
Output: 2 <br>
Explanation: The binary representation of 3 is "11". <br>
"11" -> "01" with the 2nd operation since the 0th bit is 1. <br>
"01" -> "00" with the 1st operation.

Example 2:

Input: n = 6 <br>
Output: 4 <br>
Explanation: The binary representation of 6 is "110". <br>
"110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0. <br>
"010" -> "011" with the 1st operation. <br>
"011" -> "001" with the 2nd operation since the 0th bit is 1. <br>
"001" -> "000" with the 1st operation.

Constraints:

- 0 <= n <= 10<sup>9</sup>

## S

### Python

#### Solution 1

```python
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        return n ^ self.minimumOneBitOperations(n >> 1)
```

#### Solution 2

```python
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        string = str(bin(n))
        ans = 0
        lastbit = 0
        for i, bit in enumerate(string[2:]):
            if bit == '1':
                x = 0 if lastbit else 1
            else:
                x = 1 if lastbit else 0
            ans = (ans << 1) | x
            lastbit = x
        return ans
```
