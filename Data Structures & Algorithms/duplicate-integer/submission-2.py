class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            current = num
            if current in seen:
                return True
            else:
                seen.add(current)
        return False
        