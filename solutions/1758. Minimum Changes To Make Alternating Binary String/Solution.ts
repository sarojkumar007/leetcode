function minOperations(s: string): number {
  const n = s.length;
  const sArr: string[] = s.split("");
  let count: number = 0;
  for (let i = 0; i < n; i++) {
    if (sArr[i] === sArr[i + 1]) {
      // sArr[i + 1] = sArr[i + 1] === "0" ? "1" : "0";
      sArr[i + 1] = (1 - +sArr[i + 1]).toString();
      count++;
    }
  }
  return Math.min(count, n - count);
}
