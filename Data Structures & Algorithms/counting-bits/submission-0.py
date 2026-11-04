class Solution:
    def countBits(self, n: int) -> List[int]:
        liste = []
        def count_binary(number):
            counter = 0
            while number:
                number &= number-1
                counter+=1
            return counter
        
        for i in range(n+1):
            liste.append(count_binary(i))
        return liste