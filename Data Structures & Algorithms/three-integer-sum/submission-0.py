class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resultList = []
        nums.sort()

        for i in range(len(nums)):
            ptrLeft = i + 1
            ptrRight = len(nums) - 1

            while ptrLeft < ptrRight:
                total = nums[i] + nums[ptrLeft] + nums[ptrRight]

                if total == 0:
                    triplet = [nums[i], nums[ptrLeft], nums[ptrRight]]

                    if triplet not in resultList:
                        resultList.append(triplet)

                    ptrLeft += 1
                    ptrRight -= 1

                elif total < 0:
                    ptrLeft += 1

                else:
                    ptrRight -= 1

        return resultList