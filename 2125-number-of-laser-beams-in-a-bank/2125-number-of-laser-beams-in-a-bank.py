class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m =len(bank)
        prevdevicecount = 0
        laser=0
        for c in bank[0]:
            if c=='1':  prevdevicecount+=1
        for i in range(1,m):
            devicecount = 0
            for c in bank[i]:
                if c=='1':  devicecount+=1
            if  devicecount > 0 :
                laser += devicecount*prevdevicecount
                prevdevicecount = devicecount
        return laser
                