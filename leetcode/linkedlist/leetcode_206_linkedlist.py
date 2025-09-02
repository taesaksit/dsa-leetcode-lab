# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev
    
    def reversListWithStack(self, head:Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        stack = []
        curr = head
        
        while curr:
            stack.append(curr)
            curr = curr.next
    
        new_head = stack.pop()
        curr = new_head
        
        while stack:
            curr.next = stack.pop()
            curr = curr.next
        curr.next = None
        
        return new_head
    
    def createList(self , arr):
        head = ListNode(arr[0])  
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head


nums = [1, 2, 3, 4, 5]

sol = Solution()
head = sol.createList(nums)
result = sol.reversListWithStack(head)

# Display
curr = result
while curr :
    print(curr.val)
    curr = curr.next