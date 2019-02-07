#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Backtrace in python , graceful resolution
Use set() to store all the resolutions
"""


def countArrangement(N):
    # Backtrace ( much faster than countArrangement2
    def count(i, X):
        if i == 1:
            return 1
        return sum(
            count(i - 1, X - {x}) for x in X if x % i == 0 or i % x == 0)

    return count(N, set(range(1, N + 1)))


def countArrangement2(N):
    # Backtrace
    def count(i, X, Y):
        if i > N:
            return 1
        return sum(
            count(i + 1, X - {x}) for x in X if x % i == 0 or i % x == 0)

    return count(1, set(range(1, N + 1)))


def countArrangement3(N):
    # show the list if match

    def count(i, X, Y):
        """
        i -- recursion level
        X -- existing fields
        """
        if i > N:
            #           print(Y)
            return 1
        return sum(
            count(i + 1, X - {x}, Y + [x]) for x in X
            if x % i == 0 or i % x == 0)  # 循环体 -- 剪枝条件

    return count(1, set(range(1, N + 1)), [])


def queens(N):
    """
    Inspired from resolution on countArrangement
    """

    result_set = []

    def count(i, X, Y):
        """
        i: 递归栈深度(从1 开始)
        X: 解空间
        Y: 结果
        """
        if i > N:
            result_set.append(Y)
            return Y

        # 剪枝条件
        for each in [x for x in X if save_queen(x, Y)]:
            count(i + 1, X - {each}, Y + [each])

    def save_queen(point, queens):
        if queens:
            i = 1
            p = len(queens) + 1
            for each in queens:
                if abs(point - each) == abs(p - i):
                    return False
                i += 1

        return True

    count(1, set(range(1, N + 1)), [])
    return result_set


def main():
    #   res = countArrangement(8)
    #   print(res)
    #   countArrangement2(5)
    #   countArrangement3(15)
    #   print(queens(8))
    for queen in queens(8):
        print(queen)


if __name__ == '__main__':
    main()
