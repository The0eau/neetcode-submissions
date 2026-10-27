class WordDictionary:

    def __init__(self):
        self.enfant = {}
        self.fin = False

    def addWord(self, word: str) -> None:
        courant = self 
        for char in word : 
            if char not in courant.enfant:
                courant.enfant[char] = WordDictionary()
            courant = courant.enfant[char]
        courant.fin = True

    def search(self, word: str) -> bool:
        def recur(index: int, noeud: 'WordDictionary') -> bool:
            # Condition d'arrêt : on a parcouru tout le mot
            if index == len(word):
                return noeud.fin
            
            char = word[index]
            
            # Cas 1 : Caractère générique '.'
            if char == '.':
                for enfant in noeud.enfant.values():
                    if recur(index + 1, enfant):
                        return True
                return False
            
            # Cas 2 : Lettre classique
            if char not in noeud.enfant:
                return False
            
            return recur(index + 1, noeud.enfant[char])

        return recur(0, self)
