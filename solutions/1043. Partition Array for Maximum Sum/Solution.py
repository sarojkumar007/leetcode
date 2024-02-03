from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * k
        dp[0] = arr[0]

        for i in range(1, n):
            curr_max = 0
            max_at_i = 0
            for j in range(i, i - k, -1):
                if j < 0:
                    break
                curr_max = max(curr_max, arr[j])
                window_size = i - j + 1
                curr_sum = window_size * curr_max

                sub_sum = dp[(j - 1) % k] if j > 0 else dp[-1]
                max_at_i = max(max_at_i, sub_sum + curr_sum)

            dp[i % k] = max_at_i

        return dp[(n - 1) % k]