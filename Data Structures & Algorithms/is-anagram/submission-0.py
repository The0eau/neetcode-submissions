class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_ = {}
        t_ = {}
        for i in range(len(s)):
            if s[i] in s_ :
                s_[s[i]] += 1
            else : 
                s_[s[i]] = 1
            if t[i] in t_ :
                t_[t[i]] += 1
            else : 
                t_[t[i]] = 1
        if s_ == t_ :
            return True
        else : 
            return False