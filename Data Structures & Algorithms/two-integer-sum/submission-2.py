class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashtable=[]
        for i in range(len(nums)):
            if (target-nums[i]) in hashtable:
                return [hashtable.index(target-nums[i]),i]
            else:
                hashtable.append(nums[i])