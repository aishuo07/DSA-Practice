# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st = []
        st1 = []
        head = None
        while l1:
            st.append(l1.val)
            l1 = l1.next
        
        while l2:
            st1.append(l2.val)
            l2 = l2.next
        c = 0
        while st or st1:
            s = c 
            print()
            if st:
                s+=st[-1]
                st.pop()
            
            if st1:
                s+=st1[-1]
                st1.pop()
            c = 1 if s>9 else 0
            s%=10
            new = ListNode(s)
            new.next = head
            head = new
        if c:
            new = ListNode(c)
            new.next = head
            head = new
        print(head, st, st1)
        return head