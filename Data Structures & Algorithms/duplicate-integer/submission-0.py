class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vue = []
        for i in nums :
            if i in vue :
                return True
            else :
                vue.append(i)
        return False