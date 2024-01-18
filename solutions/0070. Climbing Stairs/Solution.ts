function climbStairs(n: number): number {
  let first = 1,
    second = 1;

  for (let i = 0; i < n - 1; i++) {
    const temp = first;
    first += second;
    second = temp;
  }
  return first;
}
