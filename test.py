from typing import List


def reverseString(s: List[str]) -> None:
    # 一左一右两个指针相向而行
    left = 0
    right = len(s) - 1
    while left < right:
        # 交换 s[left] 和 s[right]
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1

# s = ["h","e","l","l","o"]
# reverseString(s)
# print(s)

def palindrome(s: str, l: int, r: int) -> str:
    # 防止索引越界
    while l >= 0 and r < len(s) and s[l] == s[r]:
        # 双指针，向两边展开
        l -= 1
        r += 1
    # 返回以 s[l] 和 s[r] 为中心的最长回文串
    return s[l + 1 : r]

s = "babad"
print(palindrome(s, 0, 0))
