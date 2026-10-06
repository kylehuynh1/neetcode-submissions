class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        leftPtr, best = 0, 0
        for right in range (len(s)):
            while s[right] in seen:
                seen.remove(s[leftPtr])
                leftPtr += 1
            seen.add(s[right])
            best = max(best, right-leftPtr+1)
        return best