class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cost=0
        count=0
        for i in range (0,len(costs)):
            if cost+costs[i]<= coins:
                cost+=costs[i]
                count+=1
            else:
                break
        return count