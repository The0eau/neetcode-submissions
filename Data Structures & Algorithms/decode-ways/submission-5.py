class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        # dp[i] représente le nombre de décodages possibles pour la sous-chaîne de longueur i
        dp = [0] * (n + 1)
        
        # Cas de base
        dp[0] = 1  # Chaîne vide (1 façon)
        dp[1] = 1  # Le premier caractère est déjà vérifié non nul
        
        for i in range(2, n + 1):
            # Option 1 : Décoder 1 seul chiffre s[i-1]
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # Option 2 : Décoder 2 chiffres s[i-2..i-1]
            two_digits = int(s[i-2:i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]