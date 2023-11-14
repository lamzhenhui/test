
class Node(object):
    def __init__(self, data=None):
        self.next = None
        self.data = data


class Solution(object):
    def swapPairs(self, head):
        # ret = Node(0)

        tmp = head
        while tmp and tmp.next:
            node1 = tmp
            node2 = tmp.next
            tmp.next = node2
            node1.next = node2.next
            node2.next = node1
            tmp = node1
        return tmp


if __name__ == "__main__":
    s = Solution()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    ret = s.swapPairs(head=node1)
    print(ret.data,
          ret.next.data,
          ret.next.next.data,
          ret.next.next.next.data
          )
    print(ret)
