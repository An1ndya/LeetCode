class Solution:
    def frequencySort(self, s: str) -> str:
        charcount = defaultdict(int)
        for c in s:
            charcount[c]+=1
        #store frequqncy to character mapping 
        counttochar = defaultdict(list)
        countarr=[]
        for key in charcount.keys():
            #store count to a array
            countarr.append(charcount[key])
            #save count to char for future mapping
            counttochar[charcount[key]].append(key) 
        countarr = sorted(counttochar.keys(), reverse=True)
        #print(countarr)
        #print(counttochar)
        ans = ""
        for count in countarr:
            #take each character of same frequency 
            for char in counttochar[count]:
                #take frequency
                for i in range(count):
                    ans+= char     
        return ans 