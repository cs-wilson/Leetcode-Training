class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        maxLength = 0
        s_len = len(s)
        fullCost = 0
        start = 0
        for end in range(s_len):
            fullCost += abs(ord(s[end]) - ord(t[end]))
            if fullCost <= maxCost: 
                maxLength = max(maxLength, end - start + 1)
            while fullCost > maxCost:
                
                fullCost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
        return maxLength




        