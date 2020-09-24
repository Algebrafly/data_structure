class MyArray:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise Exception("数组超出实际元素范围")
        for i in range(self.size - 1, -1, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def insert_v2(self, index, element):
        if index < 0 or index > self.size:
            raise Exception("数组超出实际元素范围")
        # 数组扩容
        if self.size >= len(self.array):
            self.resize()
        for i in range(self.size - 1, -1, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def remove(self, index):
        if index < 0 or index > self.size:
            raise Exception("数组超出实际元素范围")
        for i in range(index, self.size):
            self.array[i] = self.array[i+1]
        self.size -= 1

    def output(self):
        for i in range(self.size):
            print(self.array[i])

    def resize(self):
        array_new = [None] * len(self.array) * 2
        for i in range(self.size):
            array_new[i] = self.array[i]
        self.array = array_new


array = MyArray(4)
array.insert_v2(0, 10)
array.insert_v2(0, 11)
array.insert_v2(1, 0)
array.insert_v2(0, 9)
array.insert_v2(0, 19)
array.insert_v2(0, 56)
# array.output()
print('array:{}'.format(array.array))
print('size:', array.size)
array.remove(1)
print('array:{}'.format(array.array))
print('size:', array.size)
