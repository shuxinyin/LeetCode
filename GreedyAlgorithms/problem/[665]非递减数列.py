# 给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。 
# 
#  我们是这样定义一个非递减数列的： 对于数组中任意的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [4,2,3]
# 输出: true
# 解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [4,2,1]
# 输出: false
# 解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10 ^ 4 
#  - 10 ^ 5 <= nums[i] <= 10 ^ 5 
#  
#  Related Topics 数组 👍 634 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def checkPossibility(self, nums):
        """
        当 nums[i] 破坏了数组的单调递增时，即 nums[i] < nums[i - 1] 时，为了让数组有序，我们发现一个规律（在上面三个例子中， nums[i] 都为 2， nums[i -1] 都为 4）：

        如例【4，2，5】的情况，当 i = 1 ，那么修改 num[i- 1] ，不要动 nums[i] ，因为nums[i]后面的元素是啥我们还不知道呢，少动它为妙。
        如例【1，4，2，5】的情况，当 i > 1 时，我们应该优先考虑把 nums[i - 1] 调小到 >= nums[i - 2] 并且 <= nums[i]。同样尽量不去修改 nums[i] ，理由同上。
        如例【3，4，2，5】的情况，当 i > 1 且 nums[i] < nums[i - 2] 时，我们无法调整 nums[i - 1] ，我们只能调整 nums[i] 到 nums[i - 1] 。
        Time O(N)
        Space O(1)
        """
        N = len(nums)
        count = 0
        for i in range(1, N):
            if nums[i] < nums[i - 1]:
                count += 1
                if i == 1 or nums[i] >= nums[i - 2]:  # 【4，2，5】 # 【1，4，2，5】
                    nums[i - 1] = nums[i]  # 这两种情况修改nums[i-1]
                else:
                    nums[i] = nums[i - 1]  # 【3，4，2，5】修改nums[i]
        print(count)
        return count <= 1


# leetcode submit region end(Prohibit modification and deletion)




if __name__ == "__main__":
    S = Solution()
    l = [3, 4, 2, 3]
    l2 = [4, 2, 3]
    l3 = [5, 7, 1, 8]
    print(S.checkPossibility(l))
