# solutions\1235. Maximum Profit in Job Scheduling

Difficulty: `hard`

Topics: `Array`, `Binary Search`, `Dynamic Programming`, `Sorting`

## Q

We have `n` jobs, where every job is scheduled to be done from `startTime[i]` to `endTime[i]`, obtaining a profit of `profit[i]`.

You're given the `startTime`, `endTime` and `profit` arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time `X` you will be able to start another job that starts at time `X`.

<br>

Example 1:

![Ex1](https://assets.leetcode.com/uploads/2019/10/10/sample1_1584.png)

```
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job.
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
```

Example 2:

![Ex2](https://assets.leetcode.com/uploads/2019/10/10/sample22_1584.png)

```
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job.
Profit obtained 150 = 20 + 70 + 60.
```

Example 3:

![Ex3](https://assets.leetcode.com/uploads/2019/10/10/sample3_1584.png)

```
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
```

Constraints:

- `1 <= startTime.length == endTime.length == profit.length <= 5 * 10`<sup>`4`</sup>
- `1 <= startTime[i] < endTime[i] <= 10`<sup>`9`</sup>
- `1 <= profit[i] <= 10`<sup>`4`</sup>

## S

### Python

#### Solution 1

```python
class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        n = len(profit)
        dp = [0] * (n + 1)
        for i, (_, s, p) in enumerate(jobs):
            j = bisect_right(jobs, s, hi=i, key=lambda x: x[0])
            dp[i + 1] = max(dp[i], dp[j] + p)
        return dp[n]
```

#### Solution 2

```python
class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]

            # CASE: don't include
            res = dfs(i+1)

            # CASE: include
            j = bisect.bisect(intervals,(intervals[i][1],-1,-1)) # binary search next StartTime, based on current endTime
            cache[i] = res = max(res,intervals[i][2]+ dfs(j)) # max of curr profit + profit of j(next startTime)
            return res

        return dfs(0)
```

### TypeScript

```typescript
function jobScheduling(
  startTime: number[],
  endTime: number[],
  profit: number[]
): number {
  const n = startTime.length;
  const f = new Array(n).fill(0);
  const idx = new Array(n).fill(0).map((_, i) => i);
  idx.sort((i, j) => startTime[i] - startTime[j]);
  const search = (x: number) => {
    let l = 0;
    let r = n;
    while (l < r) {
      const mid = (l + r) >> 1;
      if (startTime[idx[mid]] >= x) {
        r = mid;
      } else {
        l = mid + 1;
      }
    }
    return l;
  };
  const dfs = (i: number): number => {
    if (i >= n) {
      return 0;
    }
    if (f[i] !== 0) {
      return f[i];
    }
    const j = search(endTime[idx[i]]);
    return (f[i] = Math.max(dfs(i + 1), dfs(j) + profit[idx[i]]));
  };
  return dfs(0);
}
```
