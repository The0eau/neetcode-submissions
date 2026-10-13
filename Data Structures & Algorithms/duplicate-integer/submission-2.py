class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vue = set()
        for i in nums :
            if i in vue :
                return True
            else :
                vue.add(i)
        return False