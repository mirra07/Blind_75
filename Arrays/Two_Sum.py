class Solution(object):
    def twoSum(self, nums, target):
        pmap = {}
        for i, n in enumerate(nums):
            dif = target - n
            if dif in pmap:
                return [pmap[dif],i]
            pmap[n] = i
            return 
        