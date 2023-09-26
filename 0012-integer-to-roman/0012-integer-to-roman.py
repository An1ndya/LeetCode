class Solution:
    def intToRoman(self, num: int) -> str:
        hash = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M",
                4:"IV",9:"IX",40: "XL", 90:"XC", 400:"CD",900:"CM" }
        sort =[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        
        i=0
        ans=""
        while num!=0:
            if num>=sort[i]:
                ans+= hash[sort[i]]
                num-=sort[i]
            else:
                i+=1
        return ans