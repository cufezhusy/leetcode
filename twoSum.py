class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map ={}
        for i in range(0,len(nums)):
            look_for_number = target - nums[i]
            tryIdx = map.get(look_for_number)
            if tryIdx is not None:
                return (tryIdx,i)
            else:
                map[nums[i]] = i
obj = Solution()
print(obj.twoSum([3,2,4,5,2],7))
