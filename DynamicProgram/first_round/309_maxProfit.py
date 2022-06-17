class Solution:
    """
    状态：所以对于每一天i，都有可能是三种状态：
        0.不持股且当天没卖出,定义其最大收益dp[i][0];
        1.持股,定义其最大收益dp[i][1]；
        2.不持股且当天卖出了，定义其最大收益dp[i][2]；
    转移方程:
        1. dp[i][0]=max(dp[i-1][0],dp[i-1][2])
        第i天不持股且没卖出的状态dp[i][0], 没有股票且没卖，也就是说i-1也没有股票
        那么第i-1天有两种可能：i-1不持股且当天无卖出dp[i-1][0]，或者， i-1天不持股但当天卖出dp[i-1][2]
        2. dp[i][1]=max(dp[i-1][1],dp[i-1][0]-p[i])
        第i天持股dp[i][1], 今天持股，有两种可能：
            1. 昨天就持股，今天继承昨天的，也就是dp[i-1][1]
            2. 昨天不持股，是今天买入的（那这里就必定昨天没有卖，因为有冷冻期这个东西），
                所以昨天是不持股且当天没有卖出的状态 所以是dp[i-1][0]-p[i]
        3. dp[i][2]=dp[i-1][1]+p[i]
        第i天不持股且当天卖出了，这种就是昨天肯定是持股的，不然今天没法卖，而持股就只有一种状态
        昨天持股的收益+今天卖出的得到的新收益 dp[i-1][1]+p[i]
    初始状态：
        dp[0][0]=0, 第0天不持股，且没卖出，故是0
        dp[0][1]=-1*prices[0]， 第0天持股，那此时是买了股 收益是负的 -1*prices[0]
        dp[0][2]=0， 第0天不持股且当天卖出了， 那就是买入又卖出，其收益为0
    返回 return：
        最后一天的最大收益有两种可能，而且一定是“不持有”状态下的两种可能，
        把这两种“不持有”比较一下大小，返回即可
    """

    def maxProfit(self, prices: [int]) -> int:
        n = len(prices)
        dp = [[0 for i in range(3)] for j in range(n)]
        dp[0][0] = 0
        dp[0][1] = -1 * prices[0]
        dp[0][2] = 0

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = dp[i - 1][1] + prices[i]

        return max(dp[-1][0], dp[-1][2])


if __name__ == '__main__':
    d = [1, 2, 3, 0, 2]
    S = Solution()
    print(S.maxProfit(d))

    dp = [[0 for i in range(3)] for j in range(5)]
    print(dp)
