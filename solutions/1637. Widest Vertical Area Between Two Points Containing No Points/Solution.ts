function maxWidthOfVerticalArea(points: number[][]): number {
  points.sort((a, b) => a[0] - b[0]);
  let max_dist = 0;
  for (let i = 0; i < points.length - 1; i++) {
    const dist = points[i + 1][0] - points[i][0];
    if (max_dist < dist) max_dist = dist;
  }
  return max_dist;
}
