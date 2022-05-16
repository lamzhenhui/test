# -*- coding:utf-8 -*-
class DLinkNode:
    def __init__(self, k=0, v=0):
        self.k = k
        self.v = v
        self.prev = None
        self.net = None


class LRUCache(object):


    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.hash_map = dict()
        self.max_obj = capacity
        self.head = DLinkNode()
        self.tail = DLinkNode()


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # 检查是否存在 不存在返回-1
        if key not in self.hash_map:
            return -1
        # 将获取的数据节点放到最前面

        # 返回数据
    def move_head(self,Node):
        pass
    def del_tail_node(self,Node):
        pass
    def add_node(self):
        pass

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # 查询是否超出长度
        # 将末尾的链表节点清理
        # 将插入的新的链表节点添加到双向链表末尾
        # hashmap 插入一条新的记录






# Your LRUCache object will be instantiated and called as such:
if __name__ == '__main__':
    a = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    b = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    c = zip(a,b)
    print(c)
    capacity = b[0][0]
    # for item in

    ret = []
    obj = LRUCache(capacity)
    for (action, lst ) in c:
        if action =="get":
            key = lst[0]
            print(key)
            # param_1 = obj.get(key)
            # ret.append(param_1)
        if action =="put":
            key,value = lst[0],lst[1]
            print(key,value)
            # obj.put(key,value)
    # param_1 = obj.get(key)
    # obj.put(key,value)
