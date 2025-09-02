from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def createHead(self, arr):
        if not arr:
            return None

        head = ListNode(arr[0])
        curr = head

        for i in arr[1:]:
            curr.next = ListNode(i)
            curr = curr.next

        return head

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head

        while curr:
            if curr.next and curr.next.val == curr.val:  # ตรวจสอบก่อน
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


num = [1, 1, 2, 3, 4]
sol = Solution()
head = sol.createHead(num)
result = sol.deleteDuplicates(head)

curr = result
while curr:
    print(curr.val)
    curr = curr.next
