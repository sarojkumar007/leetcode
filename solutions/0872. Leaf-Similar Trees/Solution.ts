// Definition for a binary tree node.
class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function leafSimilar(root1: TreeNode | null, root2: TreeNode | null): boolean {
  function dfs(root: TreeNode | null, leaf: number[]) {
    if (!root) return;
    if (!root.left && !root.right) {
      leaf.push(root.val);
      return;
    }
    dfs(root.left, leaf);
    dfs(root.right, leaf);
  }

  const leaf1: number[] = [],
    leaf2: number[] = [];
  dfs(root1, leaf1);
  dfs(root2, leaf2);

  return (
    leaf1.length === leaf2.length &&
    leaf1.every((val, idx) => val === leaf2[idx])
  );
}
