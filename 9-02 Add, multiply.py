from sys import stdin
import copy
import operator


class Matrix:

    def __init__(self, matrix_list):
        # self.matrix_list = matrix_list
        # self.matrix_list = matrix_list.copy()
        self.matrix_list = copy.deepcopy(matrix_list)

    def __str__(self):
        return '\n'.join(map(lambda x: '\t'.join(map(str, x)),
                             self.matrix_list))

    def size(self):
        return len(self.matrix_list), len(self.matrix_list[0])

    @staticmethod
    def sum_of_lines(line1, line2):
        return list(map(lambda c, d: operator.add(c, d), line1, line2))

    def __add__(self, other):
        # Здесь в принципе нам вообще не нужно создавать поле класса self.sum
        # Нам в задании не требуется реализовать возможность к нему обращаться.
        # Поэтому здесь можно обойтись обычной локальной переменной:
        sum1 = list(map(Matrix.sum_of_lines, self.matrix_list,
                        other.matrix_list))
        # То же самое касается и функции реализующей умножение.
        # Но её я менять не буду.
        return Matrix(sum1)

    @staticmethod
    def mul_line_on_int(line, num):
        return list(map(lambda a: operator.mul(a, num), line))

    @staticmethod
    def mul_line_on_float(line, num):
        return list(map(lambda a: float('{0:.6f}'.format(operator.mul(a, num))),
                        line))

    def __mul__(self, num):
        if isinstance(num, int):
            self.mul = list(map(lambda a: Matrix.mul_line_on_int(a, num),
                                self.matrix_list))
            return Matrix(self.mul)
        self.mul = list(map(lambda a: Matrix.mul_line_on_float(a, num),
                            self.matrix_list))
        return Matrix(self.mul)

    __rmul__ = __mul__


# m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
# print(m1 + m2)
#
# m = Matrix([[1, 1, 0], [0, 2, 10], [10, 15, 30]])
# alpha = 15
# print(m * alpha)
# print(alpha * m)

# print(m)


exec(stdin.read())

# m = Matrix([[1, 0]])
# print(m)
# m = Matrix([[2, 0, 0]])
# print(m)
# print(repr(m))
# repr - выведет только индекс объекта в памяти, т.к. у нас в классе нет метода __repr__.

# m = Matrix([[1], [0]])
# print(m)
# m = Matrix([[2], [0], [0]])
# print(m)
# print(m.size())
#

# Такой ответ в 3-м тесте он не принимает:
# 15.0	15.0	0.0
# 0.0	30.0	150.0
# 150.0	225.0	450.0
# 15.0	15.0	0.0
# 0.0	30.0	150.0
# 150.0	225.0	450.0
# (Если там float'ы)

# Сделал с разбиением на int и float
