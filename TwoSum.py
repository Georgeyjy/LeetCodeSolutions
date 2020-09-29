# problem url: https://leetcode.com/problems/two-sum/submissions/

# first solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            fill = target - nums[i]
            if fill in nums and i != nums.index(fill):
                j = nums.index(fill)
                break
        return [i, j]

# better version:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for idx, num in enumerate(nums):
            n = target - num
            if n not in dic:
                dic[num] = idx
            else:
                return [dic[n], idx]
                