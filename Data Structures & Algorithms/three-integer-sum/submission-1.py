class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for i in range (len(nums)):

            leftPtr = i + 1
            rightPtr = (len(nums)-1)

            while rightPtr > leftPtr:
                total = nums[i] + nums[leftPtr] + nums[rightPtr]

                if total == 0:
                    triplets = [nums[i], nums[leftPtr], nums[rightPtr]]
                    if triplets not in results:
                        results.append([nums[i], nums[leftPtr], nums[rightPtr]])
                    leftPtr += 1
                    rightPtr -= 1
                elif total > 0:
                    rightPtr -= 1
                else:
                    leftPtr += 1
        return results