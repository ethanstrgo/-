class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def recurse(head):
    if head is None or head.next is None:
        return head
    pre = head
    cur = head.next
    pre.next = None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
     return pre
  root = recurse(head)
  while root:
    print root.data
    root = root.next
