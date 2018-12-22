import pprint
from swiftclient.client import Connection

"""
reference : https://docs.openstack.org/python-swiftclient/latest/client-api.html#examples
"""

pretty_print = pprint.PrettyPrinter(indent=4).pprint

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

def get_object(conn,container,object):
    """docstring for get_object"""
    pass
    

if __name__ == '__main__':
    conn = get_connection_v1("test:tester","testing")
    get_account_info(conn)
    __import__('ipdb').set_trace()
