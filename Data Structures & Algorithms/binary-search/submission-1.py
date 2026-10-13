class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index_min = 0
        index_max = len(nums)
        while index_min < index_max:
            mean = (index_max + index_min)//2
            if nums[mean] == target :
                return mean
            elif nums[mean] < target:
                index_min = mean +1
            else : 
                index_max = mean
        return -1