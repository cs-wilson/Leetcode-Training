#
# @lc app=leetcode.cn id=1695 lang=python3
#
# [1695] 删除子数组的最大得分
#

# @lc code=start
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left, right = 0 ,0 
        sum_, max_grade = 0 , 0
        n = len(nums)
        occ = set()
        while right < n:
            while nums[right] in occ:
                occ.remove(nums[left])
                sum_ -= nums[left]
                left += 1
            occ.add(nums[right])
            sum_ += nums[right]
            right += 1
            max_grade = max(max_grade, sum_)
        return max_grade

# @lc code=end

solution = Solution()
print(solution.maximumUniqueSubarray([4,2,4,5,6]))