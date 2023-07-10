class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 定义最值和字符长度
        n = len(s2)
        # 定义hash存储s1的子串和s2
        s1_dict = dict()
        s2_dict = dict()
        for letter in s1:
            s1_dict[letter] = s1_dict.setdefault(letter, 0 ) + 1
        
        # 定义窗口边界
        left, right = 0, 0

        # 循环维护变量
        while right < n:
            s2_dict[s2[right]] = s2_dict.setdefault(s2[right], 0) + 1
            right += 1

            if s1_dict == s2_dict:
                return True

            if right - left > len(s1) - 1:
                s2_dict[s2[left]] -= 1
                if s2_dict[s2[left]] == 0:
                    del s2_dict[s2[left]]
                left += 1


            
        return False






solution = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(solution.checkInclusion(s1,s2))
