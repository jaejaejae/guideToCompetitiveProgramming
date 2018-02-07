"""
R(a, b) is a range minimum query denoting the minimum array value in the range of [a, b].
The precomputation takes O(nlogn).
The query takes O(1).
"""
import math


def get_highest_bit(num):
    return num.bit_length() - 1


class MinQsolver(object):
    def __init__(self, arr):
        self.__arr = arr
        self.__min_q = dict()

        self.precompute()

    def precompute(self):
        arr = self.__arr
        min_q = self.__min_q

        min_q[1] = arr[:]

        query_range = 2
        while query_range <= len(arr):
            min_q[query_range] = []
            prev_query_range = query_range >> 1
            for a in range(len(arr)):
                b = a + query_range - 1
                w = int((b - a + 1) / 2)
                if b >= len(arr):
                    break
                min_q[query_range].append(
                    min(min_q[prev_query_range][a],
                        min_q[prev_query_range][a+w]))
            query_range = query_range << 1

    def get_range_min_query(self, a, b):
        if a == b:
            return self.__arr[a]

        min_q = self.__min_q
        l = b - a + 1
        k = 1 << (get_highest_bit(l))
        return min(min_q[k][a], min_q[k][b-k+1])


if __name__ == '__main__':
    arr = [1, 3, 4, 8, 6, 1, 4, 2]
    min_q_solver = MinQsolver(arr)

    for i in range(0, len(arr)):
        print(min_q_solver.get_range_min_query(0, i))

    for i in range(3, len(arr)):
        print(min_q_solver.get_range_min_query(3, i))
