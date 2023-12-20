function buyChoco(prices: number[], money: number): number {
  prices.sort((a, b) => a - b);
  const choco_price = prices[0] + prices[1];
  return choco_price <= money ? money - choco_price : money;
}
