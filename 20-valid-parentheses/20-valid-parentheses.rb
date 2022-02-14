# @param {String} s
# @return {Boolean}
def is_valid(s)
    n=s.length
    stack = []
    puts n
    for i in 0..n
        if s[i] == '(' or s[i] == '{' or s[i] == '['
            stack.push(s[i])
        elsif s[i] == ')'
            if stack.pop!='('; return false end
        elsif s[i] == '}'
            if stack.pop!='{'; return false end
        elsif s[i] == ']'
            if stack.pop!='['; return false end
        end
    end
    stack.empty?   ?  true : false
end