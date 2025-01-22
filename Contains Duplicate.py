#Given an integer array nums, return true if any value appears more than once in the array,
# otherwise return false.
 class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #my logic is i created the list of value 
        a = list()
        for i in nums:
         #if the value which is already present in list 
         # it give true that means contain duplicate other wise false
            if i in a:
                return True
            else:
                a.append(i)
                
            
        return False
        
sol = Solution()
nums =[1,2,3,3]
sol.hasDuplicate(nums)
