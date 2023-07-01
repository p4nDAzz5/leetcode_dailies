class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        mostWater = 0

        while left != len(height)-1 and right != 0:
            if height[right] > height[left]:
                if (right - left) * height[left] > mostWater:
                    mostWater = (right - left) * height[left]
                left += 1
            elif height[right] < height[left]:
                if (right - left) * height[right] > mostWater:
                    mostWater = (right - left) * height[right]
                right -= 1
            else:
                if (right - left) * height[right] > mostWater:
                    mostWater = (right - left) * height[right]
                left += 1
                right -= 1
        return(mostWater)