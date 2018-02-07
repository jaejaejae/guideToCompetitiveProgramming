"""
Tree structures support multiple queries:
(1) sum queries
(2) range queries
(3) updating in logarithmic times.

"""


# TODO: instead of getting highest bit
# Directly compute p_k = k&-k
def get_highest_bit(num):
    return num.bit_length() - 1


class BinaryIndexedTree(object):
    def __init__(self, arr):
        self.__arr = arr
        self.__idx = []

        self.build_index()

    def build_index(self):
        arr = self.__arr
        self.__idx = arr[:]
        idx = self.__idx
        highest_bit = get_highest_bit(len(arr))
        for l in range(1, highest_bit+1):
            width = 1 << (l-1)
            for i in range((1 << l) - 1, len(arr), 1 << l):
                idx[i] = idx[i] + idx[i - width]

    def get_range_sum_from_0(self, b):
        current_bit = get_highest_bit(b+1)
        a = (1 << current_bit) - 1
        s = 0
        while a <= b:
            s += self.__idx[a]
            while a + (1 << current_bit) > b:
                current_bit -= 1
                return s
            a += 1 << current_bit

    def get_range_sum(self, a, b):
        return self.get_range_sum_from_0(b) - self.get_range_sum_from_0(a-1)


if __name__ == '__main__':
    arr = [1, 3, 4, 8, 6, 1, 4, 2]
    tree = BinaryIndexedTree(arr)

    print("sum_from_range_0:")
    for i in range(len(arr)):
        print(i, tree.get_range_sum_from_0(i))

    print("range_sum", tree.get_range_sum(3, 5))
