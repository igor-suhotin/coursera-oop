from sys import stdin
import copy


class Matrix:

    def __init__(self, matrix_list):
        # self.matrix_list = matrix_list.copy()
        self.matrix_list = copy.deepcopy(matrix_list)

    def __str__(self):
        return '\n'.join(map(lambda x: '\t'.join(map(str, x)),
                             self.matrix_list))

    def size(self):
        return len(self.matrix_list), len(self.matrix_list[0])


# a = [[1, 0], [0, 1]]
# m = Matrix(a)
# a = [[-10, 20, 50, 2443], [-5235, 12, 4324, 4234]]

# a.append([123, 1231])

# Сначала у меня условие на копирование не выполнялось!
# Здесь мы добавили в список еще один элемент, и матрица поменялась!
# Чтобы это исправить в конструкторе напишем:
# self.matrix_list = copy.deepcopy(matrix_list)

# m = Matrix([[1, 0], [0, 1]])
# m = Matrix([[-10, 20, 50, 2443], [-5235, 12, 4324, 4234]])

exec(stdin.read())

# m = Matrix([[1, 0]])
# print(m)
# m = Matrix([[2, 0, 0]])
# print(m)

# m = Matrix([[1], [0]])
# print(m)
# m = Matrix([[2], [0], [0]])
# print(m)
# print(m.size())
