class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPtr = 0
        rightPtr = len(numbers)-1

        indexList = []

        while leftPtr < rightPtr:
            if numbers[leftPtr] + numbers[rightPtr] == target:
                indexList.append(leftPtr + 1)
                indexList.append(rightPtr + 1)
                return indexList
            elif numbers[leftPtr] + numbers[rightPtr] > target:
                rightPtr -= 1 #sol too big
            else:
                leftPtr += 1 #sol not found in current iteration

        return indexList