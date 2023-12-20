from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # prices.sort() # OR
        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    prices[i], prices[j] = prices[j],prices[i]
        
        choco_price = prices[0] + prices[1]
        return money if money < choco_price else money - choco_price