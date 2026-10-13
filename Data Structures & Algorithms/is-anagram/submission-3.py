class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreq = {}
        tFreq = {}

        for c in range (len(s)):
            char = s[c]
            sFreq[char] = sFreq.get(char, 0) + 1
        
        for c in range (len(t)):
            char = t[c]
            tFreq[char] = tFreq.get(char, 0) + 1

        if sFreq == tFreq:
            return True
        else:
            return False
        