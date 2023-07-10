#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                occ.add(s[rk + 1])
                rk += 1
            ans = max(ans, rk - i + 1)
        return ans
    def lengthOfLongestSubstring2(self, s: str) -> int:
        window = defaultdict(int)  # 用于记录窗口中各字符出现的次数
        left, right = 0, 0  # 窗口的左右边界
        res = 0  # 用于记录结果

        while right < len(s):
            window[s[right]] += 1  # 更新窗口和字符的出现次数
            right += 1
            # 判断窗口是否需要收缩
            while window[s[right]] > 1:
                window[s[left]] -= 1  # 更新窗口和字符的出现次数
                left += 1
            res = max(res, right - left)  # 更新结果
        return res    

# @lc code=end
solution = Solution()
print(solution.lengthOfLongestSubstring2("abcabcbb"))

