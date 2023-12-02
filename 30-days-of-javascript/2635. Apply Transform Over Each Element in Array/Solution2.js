/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function (arr, fn) {
  let modified = [];
  for (let i = 0; i < arr.length; i++) {
    modified.push(fn(arr[i], i));
  }
  return modified;
};
