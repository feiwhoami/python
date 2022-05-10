from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index= {}
        
        for idx, x in enumerate(nums):
            if target - x in value_index:
                return [value_index[target - x], idx]
            else:
                value_index[x] = idx
        
        return []

# Run and Test
s = Solution()    
print (s.twoSum([3,3], 6))
