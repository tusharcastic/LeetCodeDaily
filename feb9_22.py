class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        if k==0:
            d = {}
            for i in nums:
                if i in d:
                    d[i]+=1
                else:
                    d[i] = 1
            c=0
            for i,j in d.items():
                if j>=2:
                    c+=1
            return c
        
        
        elif k>0:
            c=0
            d={i for i in nums}
            
            for i in d:
                if (i+k) in d:
                    c+=1
            return c
                    
            
            
            
        
#used hashing very important, similiar to concept used in 2 sum problem
