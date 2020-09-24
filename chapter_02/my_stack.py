class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


'''
使用python的列表做一个栈
'''


class MyStackV2:
    def __init__(self, limit=10):
        self.stack = []  # 存放元素
        self.limit = limit  # 栈容量极限

    def push(self, data):
        if len(self.stack) >= self.limit:  # 判断栈是否溢出
            print('StackOverflowError')
            pass
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from an empty stack')  # 空栈不能被弹出

    def peek(self):  # 查看堆栈的最上面的元素
        if self.stack:
            return self.stack[-1]

    def is_empty(self):  # 判断栈是否为空
        return not bool(self.stack)

    def size(self):  # 返回栈的大小
        return len(self.stack)


class MyStack:
    def __init__(self):
        self.size = 0
        self.top = None

    def append(self, data):
        node = Node(data)
        if self.size == 0:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

    def pop(self):
        rm_node = self.top
        self.top = self.top.next
        self.size -= 1
        return rm_node

    def output(self):
        p = self.top
        while p is not None:
            print(p.data)
            p = p.next


# 简单测试
stack = MyStack()
stack.append(2)
stack.append(3)
stack.append(5)
stack.append(10)
stack.output()
print('----------')
stack.pop()
stack.output()
