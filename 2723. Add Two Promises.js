/*
Given two promises promise1 and promise2, return a new promise.
 promise1 and promise2 will both resolve with a number. 
 The returned promise should resolve with the sum of the two numbers. 
 */
/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    /*var a,b;
    await promise1.then(r => a=r)
    await promise2.then(r => b=r)*/
    var [a, b] = await Promise.all([promise1, promise2]);
    return new Promise((resolve, reject) => {
        resolve(a+b);
    })
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */