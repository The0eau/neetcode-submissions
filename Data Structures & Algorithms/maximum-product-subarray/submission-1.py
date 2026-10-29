class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        products = [nums[0]]
        max_ = nums[0]
        min_ = [nums[0]]
        for i in range(1,len(nums)):
            max_local = max(products[i-1]*nums[i], nums[i],min_[i-1]*nums[i])
            min_local = min(products[i-1]*nums[i], nums[i],min_[i-1]*nums[i])
            products.append(max_local)
            min_.append(min_local)
            max_ = max(max_,max_local)
        return max_