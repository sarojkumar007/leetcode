function isPathCrossing(path: string): boolean {
  let [x, y] = [0, 0];
  const paths: Set<number> = new Set();
  // Starting Point
  paths.add(0);
  for (const d of path) {
    if (d === "N") y++;
    else if (d === "S") y--;
    else if (d === "E") x++;
    else if (d === "W") x--;

    const point = x * 20000 + y; // 20000 Constraint OR any High No
    if (paths.has(point)) return true;
    paths.add(point);
  }
  return false;
}
