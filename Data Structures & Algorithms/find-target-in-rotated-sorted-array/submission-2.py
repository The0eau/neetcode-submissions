class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            middle = (left+right)//2
            if target == nums[middle]:
                return middle
            if nums[middle] >= nums[left]:
                if nums[middle]> target >= nums[left]:
                    right = middle -1
                else :
                    left = middle +1
            else :
                if nums[right] >= target > nums[middle]:
                    left = middle +1
                else : 
                    right = middle - 1
        if nums[left] == target:
            return left
        else:
            return -1
        