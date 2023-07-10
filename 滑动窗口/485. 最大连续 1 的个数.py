from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLength = 0
        one_val = 0
        right = 0
        while right < len(nums):
            if nums[right] == 1:
                one_val += 1    
            maxLength = max(maxLength, one_val)
            if nums[right] == 0:
                one_val = 0
            right += 1
        return maxLength


solution = Solution()
nums = [1, 1, 0, 1, 1, 1]
print(solution.findMaxConsecutiveOnes(nums))