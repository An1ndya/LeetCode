class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n =len(nums)
        
        #if n==0:  return 0
        
        hash = {}
        
        ans=0
        
        for i in nums: 
            hash[i]=True

        for i in hash:
            
            if hash[i]:
                count=1
                #iterate forward
                number = i+1
                while number in hash:
                    count+=1
                    hash[number]=False
                    number+=1
                #iterate backward   
                number = i-1     
                while number in hash:
                    count+=1  
                    hash[number]=False
                    number-=1
                #set hash to false no element check for twice , save time    
                hash[i] = False
                
                if count> ans: ans= count
                    
        return ans