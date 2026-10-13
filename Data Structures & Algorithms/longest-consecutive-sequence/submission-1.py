class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        liste = []
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                liste.append(1)
            elif nums[i+1] == nums[i]:
                liste.append(2)
            else:
                liste.append(0)
        max_ = 1
        current = 1
        for i in liste :
            if i == 1:
                current += i
            elif i == 0 : 
                max_ = max(max_,current)
                current = 1
        return max(max_,current)
