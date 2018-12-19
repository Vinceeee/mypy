import itchat

def main():

    itchat.auto_login(hotReload=True) # 缓存登录信息，短时间不用重复扫码
    itchat.send_msg(msg="itchat登录成功",toUserName="filehelper")

    itchat.search_friends()

def getContactlist(itchat):
    for each in itchat.get_friends():
        # each = each.decode('utf-8')
        print("{0} -- {1} {2}".format(each['NickName'],each['RemarkName'],each['Signature'].strip()))

def getContactlist(itchat,friendname):
    friend = itchat.search_friends()


    

if __name__ == '__main__':
    main()