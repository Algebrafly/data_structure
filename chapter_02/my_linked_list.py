class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, size):
        self.size = size
        self.head = None
        self.last = None

    def get(self, index):
        if index < 0 or index >= self.size:
            raise Exception("超出链表节点范围")
        p = self.head
        for i in range(index):
            p = p.next
        return p

    def insert(self, data, index):
        if index < 0 or index >= self.size:
            raise Exception("超出链表节点范围")
        node = Node(data)
        if self.size == 0:
            # 空链表
            self.head = node
            self.last = node
        elif index == 0:
            # 插入头部
            node.next = self.head
            self.head = node
        elif self.size == index:
            # 插入尾部
            self.last.next = node
            self.last = node
        else:
            # 插入中间
            prev_node = self.get(index - 1)
            node.next = prev_node.next
            prev_node.next = node

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise Exception("超出链表节点范围")
        # 暂存被删除的节点，用于返回
        if index == 0:
            # 删除头结点
            rm_node = self.head
            self.head = self.head.next
        elif index == self.size - 1:
            # 删除尾节点
            prev_node = self.get(index - 1)
            rm_node = prev_node.next
            prev_node.next = None
            self.last = prev_node
        else:
            # 删除中间节点
            prev_node = self.get(index - 1)
            next_node = prev_node.next.next
            rm_node = prev_node.next
            prev_node.next = next_node
            self.size -= 1

        return rm_node

    def output(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next


l = LinkedList(10)
l.insert(3, 0)
l.insert(4, 0)
l.insert(31, 1)
l.insert(41, 2)
l.output()
print('list:{}'.format(l))
