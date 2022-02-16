class MyQueue
    def initialize()
        @s1 = []
        @s2 = []  
    end
=begin
    :type x: Integer
    :rtype: Void
=end
    def push(x)
        @s1.push(x)
    end
=begin
    :rtype: Integer
=end
    def pop()
        if @s2.empty? 
            while not @s1.empty?
                @s2.push(@s1.pop)
            end
        end
        return @s2.pop
    end
=begin
    :rtype: Integer
=end
    def peek()
        if @s2.empty? 
            while not @s1.empty?
                @s2.push(@s1.pop)
            end
        end
        return @s2.last
    end
=begin
    :rtype: Boolean
=end
    def empty()
        return (@s1.empty? and @s2.empty?)
    end
end

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue.new()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()