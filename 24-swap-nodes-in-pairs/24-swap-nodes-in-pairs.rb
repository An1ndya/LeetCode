# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @return {ListNode}
def swap_pairs(head)
    temp=head
    prev=nil
    while temp!=nil
        nextnode = temp.next
        if nextnode!=nil
            if prev!=nil 
                prev.next = nextnode 
            else
                head=nextnode
            end
            temp.next = nextnode.next
            nextnode.next = temp
            prev=temp
        end
        temp=temp.next
    end
    head
end