class Solution:
    def isPalindrome(self, s: str) -> bool:
        noSpace = ""

        #remove whitespaces
        for char in s:
            if char.isalnum():
                noSpace += char
        
        leftptr = 0
        rightptr = len(noSpace) - 1

        while leftptr < rightptr:
            if noSpace[leftptr].lower() != noSpace[rightptr].lower():
                return False

            leftptr+=1
            rightptr-=1
        return True