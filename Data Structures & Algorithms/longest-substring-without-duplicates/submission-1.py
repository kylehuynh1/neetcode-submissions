class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set() #current observed chars
        leftP, best = 0, 0 #left ptr and result var

        for r in range (len(s)): #op for length of string size
            while s[r] in seen: #while there are repeating characters... 
                seen.remove(s[leftP]) #remove s[left]
                leftP += 1 #and move leftPtr right 1
            seen.add(s[r])
            best = max(best, r - leftP + 1)
        return best