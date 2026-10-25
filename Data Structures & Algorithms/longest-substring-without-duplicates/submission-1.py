class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        rencontre = {}
        start = 0  # On commence à l'index 0 (plus simple en Python)
        
        for i in range(len(s)):
            char = s[i]
            
            # Si on a déjà vu le caractère ET qu'il se trouve dans notre fenêtre actuelle
            if char in rencontre and rencontre[char] >= start:
                # On déplace le début de la fenêtre juste après la dernière position de ce caractère
                start = rencontre[char] + 1
                
            # On met à jour la dernière position connue du caractère
            rencontre[char] = i
            
            # La longueur actuelle est simplement l'index actuel - le début + 1
            current_length = i - start + 1
            max_length = max(max_length, current_length)
            
        return max_length