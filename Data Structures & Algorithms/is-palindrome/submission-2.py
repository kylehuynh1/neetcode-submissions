class Solution:
    def isPalindrome(self, s: str) -> bool:
        stringNew = ""

        for char in s:
            if char.isalnum():
                stringNew += char.lower()

        left = 0
        right = len(stringNew) - 1

        while right > left:
            if stringNew[left] != stringNew[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
    
