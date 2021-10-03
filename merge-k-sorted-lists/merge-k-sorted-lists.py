# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 
        def merges(arr, arr1):
            new = ListNode(0)
            head = new
            while arr and arr1:
                if arr.val<arr1.val:
                    new.next = ListNode(arr.val)
                    new = new.next
                    arr = arr.next
                else:
                    new.next = ListNode(arr1.val)
                    new = new.next
                    arr1 = arr1.next
            while arr1:
                new.next = ListNode(arr1.val)
                new = new.next
                arr1 = arr1.next
            while arr:
                new.next = ListNode(arr.val)
                new = new.next
                arr = arr.next
            return head.next
        
        def merge(l, r):
            if l<r:
                mid = (l+r)//2
                return merges(merge(l, mid), merge(mid+1, r))
            return lists[l]
        return merge(0, len(lists)-1)