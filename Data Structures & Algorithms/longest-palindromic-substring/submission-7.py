class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start = 0
        max_len = 0

        def expand_around_center(left: int, right: int) -> int:
            # S'écarte vers l'extérieur tant que les caractères sont égaux
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Renvoie la longueur du palindrome trouvé
            return right - left - 1

        for i in range(len(s)):
            # Cas 1 : Palindrome impair (ex: "aba")
            len1 = expand_around_center(i, i)
            # Cas 2 : Palindrome pair (ex: "abba")
            len2 = expand_around_center(i, i + 1)
            
            current_max = max(len1, len2)
            
            # Mise à jour du meilleur palindrome
            if current_max > max_len:
                max_len = current_max
                # On calcule l'indice de départ du palindrome à partir de sa longueur
                start = i - (current_max - 1) // 2

        return s[start:start + max_len]