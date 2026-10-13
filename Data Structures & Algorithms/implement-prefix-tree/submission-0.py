class PrefixTree:

    def __init__(self):
        self.enfant = {}
        self.fin = False

    def insert(self, word: str) -> None:
        courant = self 
        for char in word : 
            if char not in courant.enfant:
                courant.enfant[char] = PrefixTree()
            courant = courant.enfant[char]
        courant.fin = True
    def search(self, word: str) -> bool:
        courant = self
        for char in word : 
            if char not in courant.enfant:
                return False
            courant = courant.enfant[char]
        return courant.fin

    def startsWith(self, prefix: str) -> bool:
        courant = self
        for char in prefix : 
            if char not in courant.enfant:
                return False
            courant = courant.enfant[char]
        return True
        