from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = (
            deque()
        )  # queue which can add or remove element from front and back used as the window to store max value
        res = []
        for i in range(0, len(nums)):
            if q and q[0] < i - k + 1:
                # remove first index if it is out of current window
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                # remove last element which are less than current num
                q.pop()
            q.append(i)  # add current elem at end
            if i >= k - 1:
                res.append(nums[q[0]])  # add first elem in res
        return res


# nums=[1,3,-1,-3,5,3,6,7]
# k=3
# q,res,idx,currelem
# [1] [] 0 1
# [3] [] 1 3
# [3, -1] [3] 2 -1
# [3, -1, -3] [3, 3] 3 -3
# [5] [3, 3, 5] 4 5
# [5, 3] [3, 3, 5, 5] 5 3
# [6] [3, 3, 5, 5, 6] 6 6
# [7] [3, 3, 5, 5, 6, 7] 7 7
