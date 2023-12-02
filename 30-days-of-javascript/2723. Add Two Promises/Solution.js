/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function (promise1, promise2) {
  const val1 = await Promise.all([promise1, promise2]);

  return new Promise((resolve, reject) => {
    resolve(val1.reduce((acc, item) => acc + item, 0));
  });
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
