/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function (obj) {
    // return JSON.stringify(obj)=="{}" || JSON.stringify(obj)=="[]";
    // in js array is object so Object.keys() fubnc will return the array of the element
    return Object.keys(obj).length === 0;
};