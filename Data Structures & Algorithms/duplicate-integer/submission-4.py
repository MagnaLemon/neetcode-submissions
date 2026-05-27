class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         comp=set()
         for i in nums:
            if i in comp:
                return True
            else:
                comp.add(i)
         return False