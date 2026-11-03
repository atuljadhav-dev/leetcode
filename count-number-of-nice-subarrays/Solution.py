class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        left = 0
        right = 0
        count = 0
        s = 0
        while right < len(nums):
            if nums[right] & 1:
                # faster than 5%2 101&01
                count += 1
            if count == k:
                # cond satisfy 
                tmp1 = left
                while left < len(nums) and not (nums[left] & 1):
                    # find next position of left
                    left += 1
                right += 1
                tmp2 = right
                while right < len(nums) and not (nums[right] & 1):
                    # find next positionof right
                    right += 1
                # arr=[0,0,1,0,0,1,0,0] k=2
                r = right - tmp2  # number of even no on right after cond satisfy
                l = left - tmp1  # number of even on left
                # l*r combination of each left with right even no [0,1,0,0,1,0][0,1,0,0,1,0,0][0,0,1,0,0,1,0][0,0,1,0,0,1,0,0]
                # l+r combination of each elem with nice array [1,0,0,1,0][1,0,0,1,0,0][0,1,0,0,1][0,0,1,0,0,1]
                # 1 nice array [1,0,0,1]
                # l*r+l+r+1
                # l(r+1)+1(r+1)
                # (l+1)*(r+1)
                s += (l+1)*(r+1)
                left += 1
                count -= 1
            else:
                right += 1
        return s
        # def atMost(k: int) -> int:
        #     res = 0
        #     left = 0
        #     current_odds = 0
            
        #     for right in range(len(nums)):
        #         if nums[right] % 2 != 0:
        #             current_odds += 1
                
        #         # Shrink window if we exceed k 
        #         while current_odds > k:
        #             if nums[left] % 2 != 0:
        #                 current_odds -= 1
        #             left += 1
                    
        #         # All subarrays ending at 'right' and starting anywhere from 'left' to 'right' are valid
        #         res += right - left + 1
                
        #     return res
        # #atMost(3)-atMost(2)=exact 3
        # return atMost(k) - atMost(k - 1)