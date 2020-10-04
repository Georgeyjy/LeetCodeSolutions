# problem url: https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for num in nums:
            output = output + [sorted(curr + [num]) for curr in output if sorted(curr + [num]) not in output]
        return output

# DFS solution
 class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sort_num = sorted(nums)
        checked=set()
        def dfs(space, path):
            if tuple(path) not in checked:
                result.append(path)
                checked.add(tuple(path))
            
            for i in range(len(space)):
                dfs(space[i+1:], path+[space[i]])
        result=[]
        dfs(sort_num,[])
        return result
