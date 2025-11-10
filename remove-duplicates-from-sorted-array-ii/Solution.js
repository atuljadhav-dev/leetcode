/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
    const l=nums.length;
    if (l <= 2) return l;

    let j = 2;
    for (let i = 2; i < l; i++) {

        if (nums[i] !== nums[j - 2]) {
            nums[j++] = nums[i];
        }
    }
    return j;
};
