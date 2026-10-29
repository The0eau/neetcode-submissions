class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        liste = [False] * len(s)
        for i in range(len(s)):
            for j in wordDict:
                if i+1 >= len(j) and j == s[i-len(j)+1:i+1] :
                    print("i")
                    if i+1 == len(j):
                        liste[i] = True
                    elif liste[i-len(j)] != False:
                        liste[i] = True
        return liste[-1]
