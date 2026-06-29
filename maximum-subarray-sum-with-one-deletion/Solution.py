class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        nodeletion = deletion = res = arr[0]
        for i in range(1, len(arr)):
            v1 = arr[i]
            v2 = nodeletion + arr[i]
            v3 = deletion + arr[i]
            v4 = nodeletion
            deletion = max(v3, v4)
            nodeletion = max(v1, v2)
            res = max(res, deletion, nodeletion)
        return res