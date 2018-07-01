#coding=utf-8
#! usr/bin/python

'''
    矩阵运算 02
    函数式
'''

def verifyMatrix(matrix):
    col = 0
    if isinstance(matrix[0],tuple):
        col = len(matrix[0])
    for eachrow in matrix:
        if  not isinstance(eachrow,tuple):
            return False
        if col != len(eachrow):
            return False
    return True

def addMatrix(matrix1,matrix2):
    res = True
    result = list()
    if not (verifyMatrix(matrix1) and verifyMatrix(matrix2)):
        print ' Invalid input , matrix is in invalid format '
        res = False
    if not ( len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0])):
        print ' The row and col not match between these two matrixes '
        res = False
    if res :
        for eachrow1,eachrow2 in zip(matrix1,matrix2):
            newrow = [x+y for x,y in zip(eachrow1,eachrow2)]
            result.append(newrow)
        print result


if __name__ == '__main__':
    matrix = ((1,2),(1,2))
    print verifyMatrix(matrix)
    matrix = ((1,2),(1,))
    print verifyMatrix(matrix)
    matrix = ((1,2),1)
    print verifyMatrix(matrix)

    matrix1 = ((1,2,3),(1,1,))
    matrix2 = ((2,3,4),(3,4,5))
    addMatrix(matrix1,matrix2)
