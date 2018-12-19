'''
 Chapter 7 in "Fluent Python"
 Some samples for decorator
'''

repo = set()

def func_repo(func):
    ''' 注册函数 '''
    def inner(*args,**kargs):
        print("init decorator {}".format(func.__name__))
        repo.add(func.__name__)
        return func(*args,**kargs)
    return inner
        
@func_repo
def foo(a,b):
    return (b,a)

@func_repo
def bar(b):
    return b+1

@func_repo
def printout():
    print("print 111233")


def main():
    foo(10,20)
    bar(100)
    printout()


if __name__ == '__main__':
    main()