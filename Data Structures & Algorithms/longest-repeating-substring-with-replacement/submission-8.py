class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqCount = {} #dict to hold char freq
        leftPtr, best = 0, 0

        for right in range (len(s)):
            char = s[right]
            freqCount[char] = freqCount.get(char, 0) + 1
            highestFreq = max(freqCount.values(), default = 0)

            while (right-leftPtr+1) - highestFreq > k:
                freqCount[s[leftPtr]] -= 1
                leftPtr += 1
                highestFreq = max(freqCount.values(), default = 0)
            best = max(best, right-leftPtr+1)
        return best