''' Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = { }
        for i in range(len(nums)):
            a = nums[i]
            #my logic is i create the dictionary for every element in array 
            if a in c:
                c[a]+=1
            # it get count when it is already present in dictionary
            else:
                c[a]=1
        sorted_elements = sorted(c, key=c.get, reverse=True)
        #here i get the keys of the dic and revese 
        return sorted_elements[:k]
        #  and do the slicing for top k frequent element
