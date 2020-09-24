class my_array:
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

    def output(self):
        for i in range(self.size):
            print(self.array[i])


array = my_array(4)
array.insert(0, 10)
array.insert(0, 11)
array.insert(0, 0)
array.insert(0, 9)
array.output()
