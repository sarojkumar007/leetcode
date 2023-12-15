/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function (fn) {
  const ans = {};
  for (let item of this) {
    const key = fn(item);
    if (ans[key]) ans[key].push(item);
    else ans[key] = [item];
  }
  return ans;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
