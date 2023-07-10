class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        occ = dict()
        rk , ans = -1, 0
        n = len(s)
        for i in range(n):
            while rk + 1 < n and len(occ) <= 2:
                if s[rk+1] not in occ:
                    occ[s[rk+1]] = 1
                    rk += 1
                else:
                    occ[s[rk+1]] += 1
                    rk += 1
            ans = max(ans, rk - i + 1)



solution = Solution()
print(solution.lengthOfLongestSubstringTwoDistinct("eceba"))