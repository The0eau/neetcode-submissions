class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Associe chaque fermante à son ouvrante
        mapping = {")": "(", "}": "{", "]": "["}

        for element in s:
            # Si c'est une parenthèse fermante
            if element in mapping:
                # Si la pile est vide OU si le sommet ne correspond pas
                if not stack or stack.pop() != mapping[element]:
                    return False
            else:
                # Si c'est une parenthèse ouvrante, on l'empile
                stack.append(element)

        # La pile doit être vide à la fin
        return not stack