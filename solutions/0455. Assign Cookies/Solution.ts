function findContentChildren(g: number[], s: number[]): number {
  g.sort((a, b) => b - a); // Reverse
  s.sort((a, b) => b - a); // Reverse

  let count = 0;

  for (let i = 0; i < g.length; i++) {
    if (count >= s.length) break;
    else if (g[i] <= s[count]) count++;
  }
  return count;
}
