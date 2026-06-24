class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        fruit={}
        left=0
        max_fruit=0
        for right in range (0,len(fruits)):
            fruit[fruits[right]]=fruit.get(fruits[right],0)+1
            while len(fruit)>2:
                fruit[fruits[left]]-=1
                if fruit[fruits[left]]==0:
                    fruit.pop(fruits[left]) 
                left+=1
            if len(fruit) <=2:
                max_fruit=max(max_fruit, right-left+1) 
        return max_fruit