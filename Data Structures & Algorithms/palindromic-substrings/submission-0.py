class Solution:
    def countSubstrings(self, s: str) -> int:
        

        def expand(left, right, counter):
            while left >= 0 and right < len(s) and s[left]==s[right]:
                counter+=1
                left-=1
                right+=1
            return counter
        counter = 0
        for i in range(len(s)):
            counter = expand(i, i, counter)
            counter = expand(i, i+1, counter)
        return counter