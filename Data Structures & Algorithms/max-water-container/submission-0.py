class Solution:
    def maxArea(self, heights: List[int]) -> int:
            left=0
            right=len(heights)-1
            max_wt=0
            while left<right:
                width=right-left
                min_height=min(heights[left],heights[right])
                curr=width*min_height
                max_wt=max(max_wt,curr)

                if heights[left] < heights[right]:
                    left+=1
                else:
                    right-=1

            return max_wt