class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            # On regarde si 'n' est le début d'une séquence
            if (n - 1) not in num_set:
                length = 1
                # On compte combien de consécutifs suivent
                while (n + length) in num_set:
                    length += 1
                # On met à jour le record
                longest = max(longest, length)

        return longest
