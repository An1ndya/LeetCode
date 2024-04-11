# @param {String} num
# @param {Integer} k
# @return {String}
def remove_kdigits(num, k)
    n=num.length
    if k == n ; return "0" end
    if k == 0 ; return num end 
    s=[] #monotonic stack
    
    num.each_char { |i|
        #keep only minimum one during each digit check
        while k>0 and not s.empty? and s.last > i
            s.pop
            k-=1
        end
        if not (s.empty? and i=="0"); s<< i end
    }
    #more number need to be removed
    #last ones are maximum as monotonic stack
    while k>0 and not s.empty? 
        s.pop
        k-=1
    end
    
    if s.empty? ;
        return "0" 
    else 
        return s.join 
    end
end