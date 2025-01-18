''' Given an integer array nums, return an array output where output[i] is the product
of all the elements of nums except nums[i].'''

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c = []
       
        for i in range(len(nums)):
            b=1
            for j in range(len(nums)):
                if i !=j:
                    
                    b *=nums[j] 
                
                
              
            c.append(b)
        return c
