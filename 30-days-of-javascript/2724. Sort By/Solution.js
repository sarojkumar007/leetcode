/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function (arr, fn) {
  arr.sort((a, b) => fn(a) - fn(b));

  // Doesn't work for all TestCases, O(n^2)
  // for(let i=0; i < arr.length;i++){
  //     for(let j = i; j < arr.length; j++){
  //         if(fn(arr[j]) < fn(arr[i])){ // This line does it.
  //             [arr[j],arr[i]] = [arr[i],arr[j]]
  //         }
  //     }
  // }

  return arr;
};
