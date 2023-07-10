from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        num_len = len(nums)
        left, right = 0, 0
        sum_, min_length = 0, num_len
        occ = []
        while right < num_len:
            occ.append(nums[right])
            right += 1
            while sum(occ) >= target:
                occ.remove(nums[left])
                left += 1
                min_length = min(min_length, right - left + 1)
        if min_length == num_len:
            return 0
        return min_length
    
soulution = Solution()
print(soulution.minSubArrayLen(15, [1,2,3,4,5]))