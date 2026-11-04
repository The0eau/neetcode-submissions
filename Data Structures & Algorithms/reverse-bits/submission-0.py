class Solution:
    def reverseBits(self, n: int) -> int:
        counter = 0      
        for i in range(32) :
            bit = (n >> i) & 1
            counter += 2**(31-i)*bit
        return counter