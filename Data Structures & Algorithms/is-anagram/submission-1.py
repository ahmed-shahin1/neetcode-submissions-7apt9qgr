class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashS,hashH = {},{}

        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i],0)
            hashH[t[i]] = 1 + hashH.get(t[i],0)
        return hashS == hashH
