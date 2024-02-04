class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #this variable will be used to check if substring covered all character in t
        # if notcovered <= 0 means covered all character 
        notcovered = len(t)
        charcount = {} # character count in t 
        for c in t:
            if c in charcount:
                charcount[c] += 1
            else:
                charcount[c] = 1
        l=0
        r=0
        minlen = 1000000
        ans = ""
        while r < len(s):
            #only consider a charatcer if it exist in t, otherwise next iteration 
            if s[r] in charcount:
                #for every character of t found in substring minus that value from hash
                charcount[s[r]]-=1
                if charcount[s[r]] >=0:
                    #if character count >= 0 it means
                    #subtring have match one character from t string
                    notcovered -= 1
                
            r+=1
            while notcovered <= 0:
                #length of substring 
                length = r-l;
                #if its minimum we should update substring
                if (length < minlen ):
                    minlen = length
                    ans= s[l:r]
                #only consider a charatcer if it exist in t, otherwise next iteration
                if s[l] in charcount:
                    #s[l] character should be removed from substring consideration 
                    #so update hash count frequency
                    #oposite of right side operation
                    charcount[s[l]] +=1
                    #if charcter count > 0, means in the next iteration 
                    #substring dont have all character covered from t
                    #so we will add not covered character  to 1
                    if charcount[s[l]] > 0:
                        notcovered += 1
                l+=1 
            
        return ans