function minOperations(nums: number[]): number {
  const hash: { [s: string]: number } = {};
  let ans: number = 0;

  for (const n of nums) {
    if (!(n in hash)) hash[n] = 0;
    hash[n]++;
  }

  for (const n of Object.values(hash)) {
    if (n === 1) return -1;
    ans += Math.ceil(n / 3);
  }

  return ans;
}
