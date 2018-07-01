#/usr/bin/env python
'''
Classical algorithm
Hanoi Towel 
'''

# No Import needed.
# No Global Variable.
# No Class definition.


def Hanoi( a , b , c , n ):
    '''
    a -- position for the plate need to move
    b -- destination for the plate need to reach
    c -- assistant plate
    n -- count of plate in a
    '''

    if ( n >= 1 ):
        Hanoi(a,c,b,n-1)
        Move(a,b)
        Hanoi(c,b,a,n-1)

def Move(a,b):
    print("move {0} to {1}".format(a,b))

if __name__ == '__main__':
    a = 'a'
    b = 'b'
    c = 'c'
    n = 3
    Hanoi(a,b,c,n)

