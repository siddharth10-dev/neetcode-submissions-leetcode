from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        
        for i, current_temp in enumerate(temperatures):
          
            while stack and current_temp > temperatures[stack[-1]]:
                prev_day_index = stack.pop()
                
               
                result[prev_day_index] = i - prev_day_index
                
            stack.append(i)
            
       
        return result