class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqCount = {}
        left, best = 0, 0

        for right in range (len(s)):
            char = s[right]
            freqCount[char] = freqCount.get(char, 0) + 1

            highestFrequency = max(freqCount.values(), default = 0)

            while (right - left + 1) - highestFrequency > k:
                freqCount[s[left]] -= 1
                left += 1
                highestFrequency = max(freqCount.values(), default = 0)
            best = max(best, (right-left+1))
        return best
                
