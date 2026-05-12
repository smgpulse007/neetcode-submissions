class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indMap = {}

        for ind, num in enumerate(nums):
            comp =  target - num

            if comp not in indMap:
                indMap[num] = ind
            else:
                return [indMap[comp], ind]