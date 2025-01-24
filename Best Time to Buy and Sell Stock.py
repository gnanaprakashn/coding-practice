'''
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.'''
def maxProfit( prices ) :
        re = list()
       
        for i in range(len(prices)):
        
            for j in range(i+1,len(prices)):
                #i compare the difference and add it in list one by one . get the max this is the logic
                c = prices[j] - prices[i]
                re.append(c)
                
        a = max(re)
        return a
