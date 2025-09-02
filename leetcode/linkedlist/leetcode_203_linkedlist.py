from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next

    def createHead(self, arr):
        head = ListNode(arr[0])
        curr = head
        for i in arr[1:]:
            curr.next = ListNode(i)
            curr = curr.next
        return head


# nums = [7, 7, 7, 7]
nums = [1,2,6,3,4,5,6]
sol = Solution()
head = sol.createHead(nums)
result = sol.removeElements(head, 6)

curr = result

while curr:
    print(curr.val)
    curr = curr.next
