# problem url: https://leetcode.com/problems/missing-number
# solution:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        sorted_list = sorted(nums)
        compare_list = [i for i in range(length)]
        
        for idx in range(length):
            if sorted_list[idx] != compare_list[idx]:
                return compare_list[idx]
        return compare_list[idx] + 1


# better version:
# 在n-1个数的列表中，缺失一个数之后必定增加的是n，n与所有数字及索引xor后必然剩余缺失的数字
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums) + 1
        expected_total = sum(range(length))
        return expected_total - sum(nums)