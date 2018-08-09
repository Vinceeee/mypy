#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Backtrace in python , graceful resolution
Use set() to store all the resolutions 
"""

def countArrangement(N):
    # Backtrace ( much faster than countArrangement2
    def count(i, X):
        __import__('ipdb').set_trace()
        if i == 1:
            return 1
        return sum(count(i - 1, X - {x})
                    for x in X
                    if x % i == 0 or i % x == 0)

    return count(N, set(range(1, N + 1)))

def countArrangement2(N):
    # Backtrace
    def count(i,X,Y):
        if i > N:
            return 1
        return sum(count(i+1, X - {x}) for x in X if x % i == 0 or i % x == 0)
    return count(1,set(range(1,N+1)))

def countArrangement3(N):
    # show the list if match

    def count(i,X,Y):
        """
        i -- recursion level
        X -- existing fields
        """
        if i > N:
#           print(Y)
            return 1
        return sum(count(i+1,X - {x},Y+[x]) 
                for x in X if x % i == 0 or i % x == 0) # 循环体 -- 剪枝条件

    return count(1,set(range(1,N+1)),[])

def queens(N):
    """
    Inspired from resolution on countArrangement
    """

    def count(i,X,Y):
        if i > N:
            print Y
            return 1
        return sum(count(i+1, X - {x}, Y+[x])
                for x in X if save_queen(x,Y))

    def save_queen(point,queens):
        if queens :
            i = 1
            p = len(queens) + 1
            for each in queens:
                if abs(point - each) == abs(p - i):
                    return False
                i += 1

        return True

    return count(1,set(range(1,N+1)),[])
        
def main():
#   countArrangement(5)
#   countArrangement2(5)
#   countArrangement3(15)
    print(queens(8))

if __name__ == '__main__':
    main()
