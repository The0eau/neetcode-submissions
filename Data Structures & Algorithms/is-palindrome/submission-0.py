class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        gauche, droite = 0, len(s) - 1

        while gauche < droite:
            if s[gauche] != s[droite]:
                return False
            gauche += 1
            droite -= 1

        return True