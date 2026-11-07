class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        leftPtr, best = 0, 0

        for rightPtr in range (len(s)):
            while s[rightPtr] in seen:
                seen.remove(s[leftPtr])
                leftPtr += 1
            seen.add(s[rightPtr])
            best = max(best, rightPtr-leftPtr+1)
        return best