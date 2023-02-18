# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        groupPrev=dummy
        
        while True:
            kth=self.getkth(groupPrev,k)
            if not kth:
                break
            groupNext=kth.next
            
            #reverse group
            
            prev,cur=kth.next,groupPrev.next
            
            while cur!=groupNext:
                nxt=cur.next
                cur.next=prev
                prev=cur
                cur=nxt
            tmp=groupPrev.next
            groupPrev.next=kth
            groupPrev=tmp
            
        return dummy.next
    def getkth(self,cur,k):
        while cur and k>0:
            cur=cur.next
            k-=1
        return cur

                
           