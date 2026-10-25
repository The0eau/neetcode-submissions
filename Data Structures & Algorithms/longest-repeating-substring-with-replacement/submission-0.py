class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        compteur = {}
        debut = 0
        max_frequence = 0
        longueur_max = 0
        
        for fin in range(len(s)):
            lettre_actuelle = s[fin]
            # Mettre à jour le compteur pour la lettre courante
            compteur[lettre_actuelle] = compteur.get(lettre_actuelle, 0) + 1
            
            # Garder la trace de la fréquence de la lettre la plus présente dans la fenêtre
            max_frequence = max(max_frequence, compteur[lettre_actuelle])
            
            # Taille de la fenêtre actuelle : fin - debut + 1
            # Si le nombre de lettres différentes de la plus fréquente dépasse k,
            # on doit réduire la fenêtre par la gauche
            if (fin - debut + 1) - max_frequence > k:
                lettre_gauche = s[debut]
                compteur[lettre_gauche] -= 1
                debut += 1
                
            # Mettre à jour la longueur maximale trouvée
            longueur_max = max(longueur_max, fin - debut + 1)
            
        return longueur_max