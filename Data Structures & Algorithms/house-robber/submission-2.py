class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        Liste = [nums[0], nums[1]]
        for i in range(2,len(nums)):
            Liste.append(max(Liste[:i-1])+nums[i])
        return max(Liste)