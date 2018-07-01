#coding=utf-8
#! usr/bin/python

'''
    矩阵运算
'''

class Matrix(object):
    '''
    Matrix -- 矩阵
    '''

    def __init__(self,col=0,row=0):
        self.col = col
        self.row = row
        self.lists = []
        for i in range(0,col):
            a = []
            self.lists.append(a)
            for j in range(0,row):
                a = 0
                self.lists[i].append(a)

    def display(self):
        for i in range(0,self.col):
            print self.lists[i]

    def add(self,another_matrix):
        if (self.col != another_matrix.col \
            and self.row != another_matrix.row):
            raise ValueError , "Rows and Cols unmatch."
        else:
            list = self.lists
            for i in range(0,self.row):
                for j in range(0,self.col):
                    list[i][j] += another_matrix.lists[i][j]
            matrix = Matrix(self.col,self.row)
            matrix.lists = list
            return matrix

    def mul(self,another_matrix):
        if (self.col != another_matrix.row ):
            raise ValueError , "Rows and Cols unmatch."
        else:
            list = self.lists
            for i in range(0,self.row):
                for j in range(0,self.col):
                    list[i][j] += another_matrix.lists[i][j]
            matrix = Matrix(self.col,self.row)
            matrix.lists = list
            return matrix


if __name__ == '__main__':

    matrix1 = Matrix(3,3)
    matrix2 = Matrix(3,3)
    # matrix3 = Matrix(3,3)

    matrix1.display()

    matrix1.lists[2][1] = 1
    matrix2.lists[1][2] = 1
    #
    matrix1.add(matrix2)
    #
    matrix1.display()
