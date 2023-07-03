class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        count = 0
        temp = 0
        i = 0
        while i > len(height)-1:
            cur = i+1
            while height[i] > height[cur] and cur < len(height)-1:
                temp += (height[i] - height[cur])
                cur += 1
                # if height[i] <= height[cur]:
                #     count += temp
            i = cur
            print(height[i],count)