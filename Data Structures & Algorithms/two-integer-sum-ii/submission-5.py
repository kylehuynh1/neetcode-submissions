class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPtr = 0
        rightPtr = len(numbers) - 1

        while leftPtr < rightPtr:
            total = numbers[leftPtr] + numbers[rightPtr]
            if total == target:
                return [leftPtr + 1, rightPtr + 1]
            elif total > target:
                rightPtr -= 1
            else:
                leftPtr += 1
        return solutionSet