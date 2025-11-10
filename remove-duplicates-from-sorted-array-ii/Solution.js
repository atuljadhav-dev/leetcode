/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
    let len=nums.length
    if (len <= 2) return len;

    let j = 2;
    for (let i = 2; i < len; i++) {

        if (nums[i] !== nums[j - 2]) {
            nums[j++] = nums[i];

        }
    }
    return j;
};
