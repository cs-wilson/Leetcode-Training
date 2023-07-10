import math

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 窗口长度为k，固定窗口长度，找平均数最大，需要数组内元素不断加和，窗口初始值左，右为0
        left, right = 0, 0
        sum_, max_average = 0, -math.inf
        num_len = len(nums)
        while right < num_len:
            sum_ += nums[right]
            right += 1
            while right - left == k:
                max_average = max(max_average, sum_ / k)
                sum_ -= nums[left]
                left += 1
        return max_average







solution = Solution()
nums = [1,12,-5,-6,50,3]
k=3
print(solution.findMaxAverage(nums,k))