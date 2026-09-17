class Solution:
    def isPalindrome(self, s: str) -> bool:
        stringNew = ""

        for char in s:
            if char.isalnum():
                stringNew += char.lower()

        leftPtr = 0
        rightPtr = (len(stringNew))-1

        while leftPtr < rightPtr:
            if stringNew[leftPtr] != stringNew[rightPtr]:
                return False
            else:
                leftPtr += 1
                rightPtr -= 1
        return True