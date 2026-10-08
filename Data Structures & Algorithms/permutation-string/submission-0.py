class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freq = {}
        s2Freq = {}

        if len(s1) > len(s2):
            return False
        for right in range (len(s1)):
            char = s1[right]
            s1Freq[char] = s1Freq.get(char, 0) + 1
            char = s2[right]
            s2Freq[char] = s2Freq.get(char, 0) + 1
        
        if s1Freq == s2Freq:
            return True

        for right in range(len(s1), len(s2)):
            outgoing = s2[right - len(s1)]
            s2Freq[outgoing] -= 1

            if s2Freq[outgoing] == 0:
                del s2Freq[outgoing]

            incoming = s2[right]
            s2Freq[incoming] = s2Freq.get(incoming, 0) + 1

            if s1Freq == s2Freq:
                return True

        return False