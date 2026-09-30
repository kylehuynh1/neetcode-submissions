class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqCount = {} #dict to char counts
        left, best = 0, 0  #left ptr, hold best window size

        for right in range (len(s)): #iterate thru string 1 index @tatime
            char = s[right] #current observed character
            freqCount[char] = freqCount.get(char, 0) + 1 #increment current char appearance and store to freqCount dict

            highestFreq = max(freqCount.values(), default = 0)#count for most common char

            #here, we calculate (right-left+1) -> length of the current window rn.
            #subtract by highestFreq to find letters that ARENT the most frequent.
            while (right-left+1) - highestFreq > k:
                freqCount[s[left]] -= 1 #decr. the freqency of the leftmost char
                left += 1 #move window until replacements adhere to k

                highestFreq = max(freqCount.values(), default = 0) #recalculate highestFreq just in case it changes
            best = max(best, right - left + 1) #then, calculate and if needed update best window size
        return best

