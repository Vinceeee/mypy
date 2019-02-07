import pprint
import itchat

pretty_p = pprint.PrettyPrinter(indent=4).pprint

def main():
    itchat.auto_login(hotReload=True, enableCmdQR=2) # 缓存登录信息，短时间不用重复扫码
#   itchat.send_msg(msg="itchat登录成功",toUserName="filehelper")
    with open("contact1.file",'w') as f:
        for each in itchat.get_friends():
            # each will be a User instance
#           f.write(str(each)+"\n")
            content = "{0}|{1}|{2}|{3}\n".format(each['NickName'],each['RemarkName'],each['Signature'].strip(), each['UserName'])
            f.write(content)

def getContactlist(itchat):
    for each in itchat.get_friends():
        # each = each.decode('utf-8')
        print("{0} -- {1} {2}".format(each['NickName'],each['RemarkName'],each['Signature'].strip()))

def getContactlist(itchat,friendname):
    friend = itchat.search_friends()


    

if __name__ == '__main__':
    main()
