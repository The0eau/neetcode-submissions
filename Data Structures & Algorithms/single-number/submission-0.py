class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashset = set()
        for i in nums:
            if i in hashset :
                hashset.remove(i)
            else : 
                hashset.add(i)
        return hashset.pop()