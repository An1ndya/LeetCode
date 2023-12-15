class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        isendpoint = {}
        for path in paths:
            isendpoint[path[0]]= False
            if not path[1] in isendpoint: 
                isendpoint[path[1]]= True
        for city in isendpoint.keys():
            if isendpoint[city]:
                return city
                
                
            
                