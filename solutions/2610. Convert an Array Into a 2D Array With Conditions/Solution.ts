function findMatrix(nums: number[]): number[][] {
  const hash = new Set();
  const res: number[][] = [];

  for (let item of nums) {
    if (!(item in hash)) hash[item] = 0;
    const row = hash[item];

    if (res.length === row) res.push([]);
    res[row].push(item);
    hash[item]++;
  }

  return res;
}
