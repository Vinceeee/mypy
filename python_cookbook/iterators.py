#!/usr/bin/env python3


def manual_iter():
    '''
    cookbook 4.1
    Using next() to manually control the iteration
    '''
    iters = iter([1,2,3,4,5,6,7,8,9,10,11])
    while True:
        try:
            result = next(iters)
            if result == 10:
                print("stopped")
                break
            print(result)
        except StopIteration:
            pass


def proxy_iter():
    '''
    cookbook 4.2
    Using __iter__ to define an iterable class
    '''
    class Node(object):
        def __init__(self,value):
            self.value = value
            self._children = [value]
        
        def add_child(self,node):
            if isinstance(node,Node):
                self._children.append(node.value)
            else:
                raise Exception("{0} is not Node",node)
        
        def __iter__(self):
            #Python的迭代器协议需要 __iter__() 方法返回一个实现了 __next__() 方法的迭代器对象。
            # list/tuple/set/dict ... 都是iterable,需要调用iter()方法获取其迭代器,犹如用len()获取其长度一样。
            return iter(self._children)
    
    node = Node(100)
    node.add_child(Node(200))
    node.add_child(Node(203))
    for i in node:
        print(i)
    

def generator():
    '''
    cookbook 4.3 , 4.4
    '''

    class Node(object):
        def __init__(self, value):
            self._value = value
            self._children = []

        def __repr__(self):
            return 'Node({!r})'.format(self._value)

        def add_child(self, node):
            self._children.append(node)

        def __iter__(self):
            return iter(self._children)

        def depth_first(self):
            yield self
            for c in self:
                yield from c.depth_first() # 递归输出生成器
        
        def breadth_first(self):
            output = [self]
            while output:
                cache = []
                for each in output:
                    yield each
                    for child in each:
                        cache.append(child)
                output = cache
                    
                

            
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    Looping = 0
    # for ch in root.depth_first():
    for ch in root.breadth_first():
        Looping += 1
        print(str(Looping)+" --> "+str(ch))



if __name__ == '__main__':
    generator()