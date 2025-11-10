/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
    let prev = 0;
    let pasteIdx = 1;
    let counter = 1;

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] !== nums[prev]) {
            counter = 1;
            [nums[i], nums[pasteIdx]] = [nums[pasteIdx], nums[i]];
            prev++;
            pasteIdx++;
        } else if (nums[i] === nums[prev] && counter < 2) {
            if (i - 1 !== prev) {
                [nums[i], nums[pasteIdx]] = [nums[pasteIdx], nums[i]];
            }

            prev++;
            counter++;
            pasteIdx++;
        }
    }

    return prev + 1;
};
