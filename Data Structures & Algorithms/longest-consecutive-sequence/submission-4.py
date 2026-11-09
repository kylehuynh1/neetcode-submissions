class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()

        for i in range(len(nums)): #first runs
            seen.add(nums[i])

        longest = 0 #second runs
        for num in seen:
            if num - 1 not in seen:
                current = num
                length = 1

                while current + 1 in seen:
                    current+=1
                    length+=1 
                longest = max(longest, length)
        return longest