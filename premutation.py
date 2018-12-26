# ===================================================================================
# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

# Basically I implemented the Heap's algorithm in Python
# https://en.wikipedia.org/wiki/Heap%27s_algorithm
# ===================================================================================
import copy
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.generate(len(nums),nums)


    def generate(self,n,nums):
        out = []
        if n == 1:
            return [copy.deepcopy(nums)]
        else:
            for i in range(1,n+1):
                out = out + self.generate(n-1,nums)
                if n%2 == 0:
                    nums = self.swap(nums,i-1,n-1)
                else:
                    nums = self.swap(nums,0, n - 1)
        return out

    def swap(self,nums,idx1,idx2):
        temp = nums[idx1]
        nums[idx1] = nums[idx2]
        nums[idx2] = temp
        return nums



obj = Solution()
print(obj.permute([1,2,3]))