# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：S = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
#  
# 
#  
# 
#  提示： 
# 
#  
#  S的长度在[1, 500]之间。 
#  S只包含小写字母 'a' 到 'z' 。 
#  
#  Related Topics 贪心 哈希表 双指针 字符串 👍 625 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def partitionLabels(self, S):
        '''
        1， 首先看第一个字母，找到它在串里最后的一个位置，记作last或一段的最后位置。
        2， 在从0~last这个范围里，挨个查其他字母，看他们的最后位置是不是比刚才的last或这一段的最后位置大。
        如果没有刚才的last或一段的最后位置大，无视它继续往后找。
        如果比刚才的大，说明这一段的分隔位置必须往后移动，所以我们把last或这一段的最后位置更新为当前的字母的最后位置。
        3，肯定到有一个时间（即左边搜索的index==last_index），这个last就更新不了了，那么这个时候这个位置就是我们的分隔位置。
        注意题目要分隔后的长度，我们就用last - startindex + 1。
        4，找到一个分割位，更新一下起始位置，同理搜索就行了。
        '''
        dic = {s: index for index, s in enumerate(S)}  # 存储某个字母对应地最后一个序号
        num = 0  # 直接计数
        result = []
        j = dic[S[0]]  # 第一个字符的最后位置

        for i in range(len(S)):  # 逐个遍历
            num += 1  # 找到一个就加1个长度
            if dic[S[i]] > j:  # 思路一样，如果最后位置比刚才的大，就更新最后位置
                j = dic[S[i]]
            if i == j:  # 思路一样，形式不同，这里就是找到这一段的结束了，就说明当前位置的index和这个字母在字典里的最后位置应该是相同的。
                result.append(num)  # 加入result
                num = 0  # 归0
        return result


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    from collections import Counter

    s = "ababcbacadefegdehijhklij"
    S = Solution()

    print(S.partitionLabels(s))
