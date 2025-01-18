#Given an integer array nums, return true if any value appears more than once in the array,
# otherwise return false.
 class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = list()
        for i in nums:
            if i in a:
                return True
            else:
                a.append(i)
                
            
        return False
        
sol = Solution()
nums =[1,2,3,3]
sol.hasDuplicate(nums)
