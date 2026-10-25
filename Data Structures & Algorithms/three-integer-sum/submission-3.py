class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. Trier le tableau pour utiliser les deux pointeurs et gérer les doublons
        nums.sort()
        res = []
        n = len(nums)
        
        # 2. Itérer sur le tableau en fixant le premier élément du triplet
        for i in range(n - 2):
            # Optimisation : si l'élément actuel est strictement positif, 
            # la somme avec les suivants (qui sont plus grands) ne pourra jamais être 0.
            if nums[i] > 0:
                break
                
            # Ignorer les doublons pour le premier élément du triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # 3. Initialiser les deux pointeurs
            gauche = i + 1
            droite = n - 1
            
            while gauche < droite:
                total = nums[i] + nums[gauche] + nums[droite]
                
                if total < 0:
                    # La somme est trop petite, on avance le pointeur gauche pour l'augmenter
                    gauche += 1
                elif total > 0:
                    # La somme est trop grande, on recule le pointeur droit pour la diminuer
                    droite -= 1
                else:
                    # On a trouvé un triplet valide
                    res.append([nums[i], nums[gauche], nums[droite]])
                    
                    # Ignorer les doublons pour le pointeur gauche
                    while gauche < droite and nums[gauche] == nums[gauche + 1]:
                        gauche += 1
                        
                    # Ignorer les doublons pour le pointeur droit
                    while gauche < droite and nums[droite] == nums[droite - 1]:
                        droite -= 1
                        
                    # Avancer/reculer les deux pointeurs pour chercher d'autres combinaisons
                    gauche += 1
                    droite -= 1
                    
        return res
            
        