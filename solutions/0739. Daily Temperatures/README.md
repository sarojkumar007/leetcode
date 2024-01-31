# solutions\0739. Daily Temperatures

Difficulty: `medium`

Topics: `Array`, `Stack`, `Monotonic Stack`

## Q

Given an array of integers `temperatures` represents the daily temperatures, return _an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`<sup>`th`</sup> day to get a warmer temperature_. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

<br>

Example 1:

```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

Example 2:

```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

Example 3:

```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

Constraints:

- `1 <= temperatures.length <= 10`<sup>`5`</sup>
- `30 <= temperatures[i] <= 100`

## S

### Python

```python
class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        s = [] # [temp,index]

        for i,t in enumerate(temps):
            while s and t > s[-1][0]:
                sTemp, sIdx = s.pop()
                res[sIdx] = i - sIdx
            s.append([t,i])

        return res
```
