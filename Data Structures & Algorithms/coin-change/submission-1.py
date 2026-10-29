class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 :
            return 0
        coin_list = [10000000] * (amount+1)
        coin_list[0] = 0
        for i in range(amount+1):
            for j in coins :
                if j <= i:
                    coin_list[i] = min(coin_list[i], coin_list[i-j] + 1)              
        if coin_list[amount] > amount:
            return -1
        return coin_list[amount]


        