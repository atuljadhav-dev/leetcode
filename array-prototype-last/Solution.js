/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    result=this[this.length-1]
    if (result===undefined){
        return -1
    }else {
        return result
    }
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */