__________________________________________________________________________________________________
72ms
× Close
sample 72 ms submission
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2: # 判空，如果其中一个为空，直接返回另一个链表（不知道说的对不对）
            return l1 or l2
        head = l1 # 把l1链表指向给head
        cary = 0 # 设置进位为0
        while l1 and l2: # 当链表l1 和 l2 都不为空时
            l1.val += l2.val + cary # 把l1链表的当前结点值 加上 l2链表的当前结点值与进位的和 

            if l1.val >9: # 如果此时 l1结点 的值大于9
                cary = 1 # 进位加一 （正确情况是cary = (l1.val + l2.val + cary)//10,因为进位不是必须为一，本题特俗，进位最多只能为一）
                l1.val = l1.val%10 # 在对结点 l1的值进行对10 取余，在把余数赋值给 l1
            else: # 其他情况
                cary = 0 # 进位重新设置成0（防止前面加过进位，造成进位乱加）
            last_node = l1 # 把l1链表的头结点的指向给last_node，形成单向循环链表
            l1 = l1.next 
            l2 = l2.next

        l = l1 or l2
        last_node.next = l
        while l:
            l.val += cary
            if l.val >9:
                cary = 1
                l.val = l.val%10
            else:
                cary = 0
            last_node  = l
            l = l.next
        if cary == 1:
            last_node.next = ListNode(1)
        return head
__________________________________________________________________________________________________
78ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry = 0
        prev = result = ListNode(0)
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:                
                carry += l2.val
                l2 = l2.next
            prev.next = ListNode(carry % 10)
            prev = prev.next

        return result.next
__________________________________________________________________________________________________
84ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def toint(node):
            return node.val + 10*toint(node.next) if node else 0
        def tolist(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = tolist(n//10)
            return node
        return tolist(toint(l1)+toint(l2))
__________________________________________________________________________________________________
88ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i1=0
        i2=0
        i=0
        while True:
            i1=i1+l1.val*10**i
            i+=1
            if l1.next==None:
                break
            l1=l1.next
        i=0
        while True:
            i2=i2+l2.val*10**i
            i+=1
            if l2.next==None:
                break
            l2=l2.next
        sum=i1+i2
        res=[]
        x=0
        print(sum)
        sum=str(sum)
        for i in range(len(sum)):
            if x==0:
                x=ListNode(int(sum[i]))
            else:
                y=ListNode(int(sum[i]))
                y.next=x
                x=y
        
        return x
__________________________________________________________________________________________________
12296 kb 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        
        if not l1:
            return l2
        if not l2:
            return l1

        carry = 0
        dummy = ListNode(0)
        cur = dummy
        l1Val = 0
        l2Val = 0

        while l1 or l2 or carry:

            if l1:
                l1Val = l1.val
            else:
                l1Val = 0

            if l2:
                l2Val = l2.val
            else:
                l2Val = 0

            target = l1Val + l2Val + carry

            if l1Val + l2Val + carry >= 10: 
                carry = 1
                target %= 10
            else:
                carry = 0

            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next

            s = ListNode(target)
            cur.next = s
            cur = cur.next


        return dummy.next
__________________________________________________________________________________________________
