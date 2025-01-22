''' Given an integer array nums, return an array output where output[i] is the product
of all the elements of nums except nums[i].'''

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c = []
       # i created the list to store the product of array
        for i in range(len(nums)):
            b=1
            for j in range(len(nums)):
                # i created the 2 loops for product it wont mutiple except self 
                if i !=j:
                    
                    b *=nums[j] 
                
                
              
            c.append(b)
            #append the product of array to the list
        return c
