class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = sorted(set(nums))
        b = 1
        c = 1
        if not nums :
            return 0 
        for i in range(1,len(a)):
            # my logic if the get the i and besides of the elemeny by using loop
            #if the difference exactly equal to 1 ,
            #i add the 1 to b because count the longested consecutive
            
            if a[i] - a[i-1] == 1 :
                b+=1
            
            else:
                # if not equal to goes to c and b become the 1 
                c = max(c,b)
                b =1
    
        return max(c,b)
