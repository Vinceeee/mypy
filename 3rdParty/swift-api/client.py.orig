from multiprocessing import Process
import time
import pprint
from swiftclient.client import Connection

"""
reference : https://docs.openstack.org/python-swiftclient/latest/client-api.html#examples
"""

pretty_print = pprint.PrettyPrinter(indent=4).pprint

meta_name = "x-container-meta-data"
container_meta_testdata={meta_name:2}

def get_connection_v1(user,key):
    """
    conn : swiftclient connection
    """
    _authurl = "http://127.0.0.1:8080/auth/v1.0"
    _auth_version = '1'
    _user = user
    _key = key

    conn = Connection(
        authurl=_authurl,
        user=_user,
        key=_key
            )
    
    return conn

def get_account_info(conn):
    """
    conn : swiftclient connection
    get account info
    """
    pretty_print(conn.get_account())

def get_container(conn,container):
    """
    get container info
    return (container_header_info,container)
    """
    pretty_print(conn.get_container(container))

def head_container(conn,container):
    pretty_print(conn.head_container(container))

def post_container(conn,container):
    conn.post_container()

def get_object(conn,container,object):
    """docstring for get_object"""
    pass
    

def update_meta(conn,data):
    # conn -- swiftclient connection
    # data -- int , value added to cur
    cur = int(conn.head_container("aaa").get(meta_name))
    try:
        cur += data
        container_meta_testdata = {meta_name:cur}
        conn.post_container("aaa",container_meta_testdata)
        print conn.head_container("aaa").get(meta_name)
    except Exception as e:
        raise 

def add_data(val):
    print "Add val %d to meta data" % val
    conn = get_connection_v1("test:tester","testing")
    update_meta(conn,val)

if __name__ == '__main__':
    p_list = []
    for i in range(4):
        p = Process(target=add_data,args=(i,))
        p.start()
        p_list.append(p)
    for p in p_list:
        p.join()
    conn = get_connection_v1("test:tester","testing")
    print conn.head_container("aaa").get(meta_name)
