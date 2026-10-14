class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #initialize two pointers to examine length and a variable to store max water
        #at each iteration, we are going to calculate length x width for max water and store it into maxwater var
        #the constraints make sure that water between the bars gets filled to the bar with smaller height. 
        #need to determine which of the two is smaller, then find how far away they are from each other (index) wise
        #afterwards, we are going to do smaller height as length x width (bar distance from eo), to calculate maxwater

        #how do we determine which bars are suitable and which are not ? 
        #what are the conditions we have to examine before moving the bar selection ?

        left = 0
        maxWater = 0
        right = (len(heights)) - 1
        
        while left < right:
            for bar in heights:
                smallBar = 0
                if heights[left] < heights[right]:
                    smallBar = heights[left]
                else:
                    smallBar = heights[right]

                barDistance = right - left
                maxWater =  max(maxWater, smallBar * barDistance)

                #move the smaller of the two bars inward
                if smallBar == heights[left]:
                    left += 1
                else:
                    right -= 1

            return maxWater