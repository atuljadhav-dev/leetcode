class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        smallangle=0
        minangle=minutes*6
        hourangle=hour*30+minutes*0.5
        if hourangle>minangle:
            smallangle=hourangle-minangle
        else:
            smallangle=minangle-hourangle
        if smallangle>180:
            smallangle=360-smallangle
        return smallangle
        
        