class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
            
        # Dictionnaire pour compter les caractères requis de t
        compte_t = {}
        for char in t:
            compte_t[char] = compte_t.get(char, 0) + 1
            
        # Variables pour suivre la progression
        requis = len(compte_t) # Nombre de caractères uniques de t dont on a besoin
        obtenus = 0            # Nombre de caractères uniques de t actuellement satisfaits
        
        # Dictionnaire pour la fenêtre courante
        fenetre = {}
        
        # Stocker le résultat final : (longueur_minimum, index_gauche, index_droit)
        resultat = (float("inf"), -1, -1)
        
        gauche = 0
        
        for droite in range(len(s)):
            caractere = s[droite]
            fenetre[caractere] = fenetre.get(caractere, 0) + 1
            
            # Si le caractère fait partie de t et qu'on a atteint la quantité requise
            if caractere in compte_t and fenetre[caractere] == compte_t[caractere]:
                obtenus += 1
                
            # Tant que la fenêtre contient tous les caractères requis, on essaie de la rétrécir
            while obtenus == requis:
                # Mettre à jour le résultat si on a trouvé une fenêtre plus petite
                taille_actuelle = droite - gauche + 1
                if taille_actuelle < resultat[0]:
                    resultat = (taille_actuelle, gauche, droite)
                    
                # Le caractère qu'on s'apprête à retirer de la gauche
                caractere_gauche = s[gauche]
                fenetre[caractere_gauche] -= 1
                
                # Si ce caractère faisait partie de t et qu'on n'en a plus assez, on met à jour 'obtenus'
                if caractere_gauche in compte_t and fenetre[caractere_gauche] < compte_t[caractere_gauche]:
                    obtenus -= 1
                    
                # Rétrécir la fenêtre
                gauche += 1
                
        # Extraire les indices du résultat
        longueur_min, debut, fin = resultat
        
        return s[debut:fin+1] if longueur_min != float("inf") else ""