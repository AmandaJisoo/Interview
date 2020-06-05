class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """
        s = set()
        while head:
            if head in s: return True
            s.add(head)
            head = head.next
        return False
        """
        #Pointer solution
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return True
        return False
        