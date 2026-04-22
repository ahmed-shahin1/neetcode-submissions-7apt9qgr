class Solution:
    def reverseString(self, s: List[str]) -> None:
        right, left = 0, len(s) - 1
        while right < left:
            s[right],s[left] = s[left],s[right]
            right +=1
            left -=1
        return s
