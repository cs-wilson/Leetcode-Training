from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow ,fast = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                print(nums[fast], nums[slow])
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
            fast += 1
            print(nums)



# @lc code=end
nums = [1,1,0,3,0,12]
Solution().moveZeroes(nums)
print(nums)