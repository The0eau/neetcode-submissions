class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ligne = [1]
        for i in range(1,len(nums)):
            max_ = 1
            for j in range(i):
                if nums[i] > nums[j] :
                    max_ = max(max_, ligne[j] +1)
            ligne.append(max_) 
        return max(ligne)