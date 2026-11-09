class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()

        #first run throw everything into a set
        for i in range(len(nums)):
            seen.add(nums[i])

        #second run check if the current element has a consecutive number thats in seen set
        #get a tracker to hold longest length

        longest = 0
        for num in seen:
            if num-1 not in seen:
                length = 1
                current = num

                while current + 1 in seen:
                    length+=1
                    current+=1
                longest = max(longest,length)
        return longest
        