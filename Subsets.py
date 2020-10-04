# problem url: https://leetcode.com/problems/subsets/

# 每增加一个数字，则结果中增加数组为上一次结果中的每个数组与新增数组相加产生的新数组
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]
        return output