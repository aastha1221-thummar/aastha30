class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        if not coins:
            return -1

        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for s in range(1, amount + 1):
            for coin in coins:
                if coin <= s:
                    dp[s] = min(dp[s], dp[s - coin] + 1)

        return dp[amount] if dp[amount] != INF else -1
