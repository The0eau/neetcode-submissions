class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vu = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in vu:
                return [vu[complement], i]
            vu[num] = i
        