from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        return
    
    def createHead(self, arr) :
        head = ListNode(arr[0])
        curr = head
        for i in  arr[1:] :
            curr.next = ListNode(i)
            curr = curr.next
        return  head
    
    
input = [1,2,6,3,4,5,6]
sol = Solution()
head = sol.createHead(input)

curr = head
while curr :
    print(curr.val)
    curr = curr.next