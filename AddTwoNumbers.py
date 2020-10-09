# problem url: 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        curr = res
        carry = 0
        
        while l1 or l2:
            if not l1:
                val = l2.val + carry
            elif not l2:
                val = l1.val + carry
            else:
                val = l1.val + l2.val + carry
            # 判断是否进位    
            if val >= 10:
                val %= 10
                carry = 1
            else:
                carry = 0
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # 最终存在进位则需要在链表末位添加一个1
        curr.next = ListNode(carry) if carry else None
        return res.next
