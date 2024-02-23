# solutions\0787. Cheapest Flights Within K Stops

Difficulty: `medium`

Topics: `Dynamic Programming`, `Depth-First Search`, `Breadth-First Search`, `Graph`, `Heap (Priority Queue)`, `Shortest Path`

## Q

There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [from`<sub>`i`</sub>`, to`<sub>`i`</sub>`, price`<sub>`i`</sub>`]` indicates that there is a flight from city `from`<sub>`i`</sub> to city `to`<sub>`i`</sub> with cost `price`<sub>`i`</sub>.

You are also given three integers `src`, `dst`, and `k`, return _the **cheapest price** from `src` to `dst` with at most `k` stops_. If there is no such route, return `-1`.

<br>

Example 1:

![Ex1](https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-3drawio.png)

```
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
```

Example 2:

![Ex2](https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-1drawio.png)

```
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
```

Example 3:

![Ex3](https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-2drawio.png)

```
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
```

Constraints:

- `1 <= n <= 100`
- `0 <= flights.length <= (n * (n - 1) / 2)`
- `flights[i].length == 3`
- `0 <= from`<sub>`i`</sub>`, to`<sub>`i`</sub>` < n`
- `from`<sub>`i`</sub>` != to`<sub>`i`</sub>
- `1 <= price`<sub>`i`</sub>` <= 10`<sup>`4`</sup>
- There will not be any multiple flights between two cities.
- `0 <= src, dst, k < n`
- `src != dst`

## S

### Python

```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k+1):
            tmpPrices = prices.copy()

            for s,d,p in flights: #src,dst,price
                if prices[s] == float('inf'):
                    continue

                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices

        return prices[dst] if prices[dst] != float('inf') else -1
```
