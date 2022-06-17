# 斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是： 
# 
#  
# F(0) = 0，F(1) = 1
# F(n) = F(n - 1) + F(n - 2)，其中 n > 1
#  
# 
#  给定 n ，请计算 F(n) 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 2
# 输出：1
# 解释：F(2) = F(1) + F(0) = 1 + 0 = 1
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 3
# 输出：2
# 解释：F(3) = F(2) + F(1) = 1 + 1 = 2
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 4
# 输出：3
# 解释：F(4) = F(3) + F(2) = 2 + 1 = 3
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 30 
#  
#  Related Topics 递归 记忆化搜索 数学 动态规划 👍 471 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fib(self, n: int) -> int:
        ''' DP
        状态： dp[i]表示第i项的值
        转移： dp[i] = dp[i-1] + dp[i-2]
        初始状态： dp[0]=0, dp[1]=1
        '''
        a, b = 0, 1
        if n == 0:
            return a
        if n == 1:
            return b
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return c

    def fib2(self, n: int) -> int:
        ''' 把0，1两种情况概括进来的写法
        初始状态： dp[0]=0, dp[1]=1
        n=1,  a,b = 1, 1
        n=2,  a,b = 1, 2
        ... a的值表示当前位置的值
        '''
        a, b = 0, 1

        for i in range(n):
            tmp = a
            a = b
            b = tmp + b
        return a
# leetcode submit region end(Prohibit modification and deletion)
