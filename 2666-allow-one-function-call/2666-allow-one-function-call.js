/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let iscalled = false;
    return function(...args){
        if(iscalled) return undefined;
        else{
            iscalled = true;
            return fn(...args);
        }
    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
