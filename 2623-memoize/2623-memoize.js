/**
 * @param {Function} fn
 */
function memoize(fn) {
    let dictionary = {};
    return function(...args) {
        let key = args.toString();
        if(!(key in dictionary))
        {
            dictionary[key] = fn(...args); 
        }
        return dictionary[key];
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */