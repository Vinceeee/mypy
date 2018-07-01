def decorators():
    '''
    covering chapter 9.01 -- 9.0x
    '''
    import time
    import logging
    from functools import wraps,partial
    def logtime(func):
        '''
        记录函数调用的时间
        '''
        @wraps(func)# warps 函数能记录函数的元信息,如函数名字,注解...
        def inner(*args,**kargs):
            '''
            doc from inner
            '''
            start = time.time() # return the current time in seconds since the Epoch
            result = func(*args,**kargs)
            end = time.time()
            print(func.__name__, end-start)
            return result
        return inner
    
    def attach_wrapper(obj,func=None):
        if func is None:
            return partial(attach_wrapper,obj)
        setattr(obj,func.__name__,func)
        return func

    def advanced_logtime(level,name=None,message=None):
        '''带参数的装饰器'''

        def deco(func):
            logname = name if name else func.__module__
            log = logging.getLogger(logname)
            logmsg = message if message else func.__name__

            @wraps(func)
            def inner(*args,**kargs):
                print("{0} -- {1}".format(level,logmsg))
                log.log(level,logmsg)
                return func(*args,**kargs)
            
            @attach_wrapper(inner)
            def setlevel(newlevel):
                nonlocal level
                level = newlevel
            return inner
        return deco

    @logtime
    @advanced_logtime(logging.DEBUG)
    def testingFunc():
        '''
        doc from testingFunc
        '''
        print("do Something ...")
    
    @logtime
    @advanced_logtime(logging.CRITICAL)
    def testingFunc2():
        for i in range(10000):
            pass
        print("do Something again ...")

    testingFunc()
    testingFunc2()
    testingFunc.setlevel(logging.INFO)
    testingFunc()

def decorators2():
    import time
    import logging
    from functools import wraps,partial

    logging.basicConfig(format="%(asctime)-15s %(message)s")

    def logged(func=None,*,level=logging.DEBUG,name=None,msg=None):
        if func is None:
            return partial(logged,level=level,name=name,msg=msg)
        
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = msg if msg else func.__name__

        @wraps(func)
        def wrapper(*args,**kargs):
            log.log(level,msg)
            return func(*args,**kargs)
        
        return wrapper

    @logged(level=logging.CRITICAL,msg="this is my horse")
    def foo(x,y):
        return "{0} -- {1}".format(x,y)

    @logged
    def bar():
        pass
        
    foo(1,2)
    bar()


def main():
    decorators2()

if __name__ == '__main__':
    main()