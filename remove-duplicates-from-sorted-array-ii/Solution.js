/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
    const l=nums.length;
    if (l <= 2) return l;

    let k = 2;
    for (let i = 2; i < l; i++) {
        if (nums[i] !== nums[k - 2]) {
            nums[k++] = nums[i];
        }
    }
    return k;
};
