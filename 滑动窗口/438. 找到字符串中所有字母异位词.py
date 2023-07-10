
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict = dict()
        for letter in p:
            p_dict.setdefault(letter, 0)
            p_dict[letter] += 1
        
        
        s_dict = dict()
        left, right = 0, 0
        s_len = len(s)
        valid_index = []
        while right < s_len:
            s_dict[s[right]] = s_dict.setdefault(s[right], 0) + 1
            if s_dict == p_dict:
                valid_index.append(left)
            right += 1          

            if right > len(p) - 1:
                s_dict[s[left]] -= 1
                if s_dict[s[left]] == 0:
                    del s_dict[s[left]]
                left += 1
                    
        return valid_index
        



soulution = Solution()
s = "cbaebabacd"
s1 = "baa"
p = "abc"
p1 = "aa"
print(soulution.findAnagrams(s, p))