from sys import stdin
import copy
import operator


class MatrixError(BaseException):
    def __init__(self, first_matrix, second_matrix):
        self.matrix1 = first_matrix
        self.matrix2 = second_matrix


class Matrix:

    def __init__(self, matrix_list):
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
        # можно было написать так:
        # if self.size() == Matrix.size(other):
        # или, например, так:
        # if Matrix.size(self) == other.size():
        if Matrix.size(self) == Matrix.size(other):
            self.sum = list(map(Matrix.sum_of_lines, self.matrix_list,
                                other.matrix_list))
            return Matrix(self.sum)
        else:
            raise MatrixError(self, other)

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

    def transpose(self):
        # matrix_for_transpose = copy.deepcopy(self.matrix_list)
        self.matrix_list = list(map(lambda *args: list(args),
                                    *self.matrix_list))
        return Matrix(self.matrix_list)

    def transposed(self):
        return Matrix(list(map(lambda *args: list(args), *self.matrix_list)))

    __rmul__ = __mul__


exec(stdin.read())

