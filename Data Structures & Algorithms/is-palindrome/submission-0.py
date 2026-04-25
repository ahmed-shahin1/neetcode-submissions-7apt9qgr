class Solution:
    def isPalindrome(self, s: str) -> bool:
        validStr = ""
        for letter in s:
            if letter.isalnum():
                validStr += letter.lower()
        return validStr == validStr[::-1]