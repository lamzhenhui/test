
class Node(object):
    def __init__(self, data=None):
        self.next = None
        self.data = data


class Solution(object):
    def hiscycly(self, head):
        a = b = head
        while a.next or b.next.next:
            a = a.next
            b = b.next.next
            if a == b:
                return True
        return False


if __name__ == "__main__":
    s = Solution()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node2
    node2.next = node3
    node3.next = node2
    ret = s.hiscycly(head=node1)
    print(ret)
