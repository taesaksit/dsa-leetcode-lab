from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def createHead(self, arr):
        head = ListNode(arr[0])
        curr = head
        for i in arr[1:]:
            curr.next = ListNode(i)
            curr = curr.next
        return head


nums = [1, 2, 3, 4, 5]
sol = Solution()
head = sol.createHead(nums)
result = sol.middleNode(head)


# display
current = result
while current.next:
    print(current.val)
    current = current.next
