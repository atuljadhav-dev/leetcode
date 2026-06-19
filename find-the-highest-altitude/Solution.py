class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitudes=[0]
        n=0
        for i in gain:
            n=n+i
            altitudes.append(n)
            
        return max(altitudes)