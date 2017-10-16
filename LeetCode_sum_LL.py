# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        total = 0
        rev_result = 0
        carry = 0
        mf = 10
        head = curr = ListNode(0)
        
        while l1 is not None or l2 is not None:
                #print("l1: ", l1.val, " l2: ",l2.val)
                x = l1.val if l1 is not None else 0
                y = l2.val if l2 is not None else 0
                total = carry + x + y
                print("Total: ", total)
                carry = total // 10
                print("carry: ", carry, "remainder:", total%10)
                curr.next = ListNode(total%10)
                curr = curr.next
                if l1:
                    l1 = l1.next 
                if l2:
                    l2 = l2.next 
                continue
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next

def test():
    print("Num1:", str(18))
    print("Num2:", str(0))
    a = ListNode(1)
    b = ListNode(8)
    a.next = b
    
    a1 = ListNode(0)
        
       
    x = Solution()
    return x.addTwoNumbers(a,a1)
    

r = test()

while r is not None:
    print(r.val, end="")
    r = r.next