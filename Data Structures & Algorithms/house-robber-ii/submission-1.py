class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        liste = [nums[0], nums[1]]
        one_position = [True, False]
        for i in range(2, len(nums)-1):
            max_i = max(liste[:i-1])
            if one_position[liste.index(max_i)]:
                one_position.append(True)
            else:
                one_position.append(False)
            liste.append(max_i+nums[i])
        max_i = max(
    (liste[i] - liste[0] if one_position[i] else liste[i]) 
    for i in range(len(liste) - 1)
)
        max_i = max_i + nums[-1]
        liste.append(max_i)
        return max(liste)