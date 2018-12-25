class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        pos_nums = [x for x in nums if x > 0]
        if len(pos_nums) == 0: return 1
        max_num = max(pos_nums)
        if max_num < 1: return 1
        for i in range(1, max_num):
            if i not in pos_nums: return i
        return max_num + 1


obj = Solution()
print(obj.firstMissingPositive([-3,1,5]))