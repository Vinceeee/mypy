import time
import redis
from redis import WatchError

'''
for python-redis , SELECT statement had not been implemented .
It is not safe to pass PubSub or Pipeline objects between threads.
'''

LOCALHOST = '127.0.0.1'

def testSimpleCase():
    # use connection pool 
    pool = redis.ConnectionPool(host=LOCALHOST)
    c = redis.Redis(connection_pool=pool,db=0) # choose db sequence

    # clear all records in DB
    c.flushdb()

    # get / set a key-value , use incr / decr for counting
    c.set(name="Saving",value=10)
    c.incr('Saving')
    c.incr('Saving')
    c.incr('Saving') # atomic operation , fullfill Linearizability
    print("Saving is {}".format(c.get('Saving')))    
    c.decr('Saving')
    c.decr('Saving')
    c.decr('Saving')
    c.decr('Saving')
    print("Saving is {}".format(c.get('Saving')))    


def testPipeline():
    pool = redis.ConnectionPool(host=LOCALHOST)
    c = redis.Redis(connection_pool=pool,db=0) # choose db sequence

    pipe = c.pipeline()
    pipe.set("aaa","bbb")
    pipe.set("ccc","ddd")
    pipe.get("eee")

    print(pipe.execute())

def testWatchTraction():
    pool = redis.ConnectionPool(host=LOCALHOST)
    c = redis.Redis(connection_pool=pool,db=0) 

    with c.pipeline() as pipe:
        while True:
            # transaction to watch a key
            # if the key has been changed during the transaction , 
            # a WatchError will be raised
            try:
                pipe.watch("WATCH")
                v = pipe.get("WATCH")
                if not v :
                    v = 1
                else:
                    v = int(v)
                    v += 1
                pipe.multi()
                pipe.set("WATCH",v)
                pipe.execute()
                break
            except WatchError:
                print("Key has been changed ... retry again ...")
                time.sleep(1)
                continue

def producer():
    pool = redis.ConnectionPool(host=LOCALHOST)
    c = redis.Redis(connection_pool=pool,db=0) 

    with c.pipeline() as pipe:
        c.incr('product')

def main():
#   testSimpleCase()
#   testPipeline()
    testWatchTraction()

if __name__ == '__main__':
    main()
