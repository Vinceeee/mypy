'''
    python3 cookbook chap 2 strings
    http://python3-cookbook.readthedocs.io/zh_CN/latest/c02/p02_match_text_at_start_end.html
'''
def _21():
    '''
    使用多个界定符分割字符串
    '''
    lines = "sadfkl xzclkv;sad fjasidf     cvjk109 asdkjf"
    import re
    result = re.split(r'[;,\s]\s*',lines) # 不保留分割符号
    print(result)
    result = re.split(r'(;|,|\s)\s*',lines) # 保留分割符号,使用正则分组特性
    delimeters = result[1::2]
    result = result[::2]
    print(delimeters)
    print(result)

def _22():
    '''
    匹配字符串开头或结尾
    '''
    filename = 'xxxyy.avi'
    print(filename.startswith("xx"))
    print(filename.endswith(".avi"))
    url = "http://8.8.8.8"
    print(url.endswith(".com")) 

    filetype = ('.jpeg','.avi','.mp3','.png')
    filenames = ['a.jpeg','bbb.avi','hello.cpp']
    for each in (x for x in filenames if x.endswith(filetype)):
        print(each)

def _23():
    '''
    用shell通配符匹配字符串
    '''
    from fnmatch import fnmatch
    print(fnmatch("GLE.IN.OBS.PRD01.LEIS.A0101","*OBS*")) # case sensitive 

def _24():
    '''
    字符串匹配
    '''
    import re
    text1 = "18/02/2018" 
    if re.match(r'\d+/\d+/\d+',text1):
        print("Yes")
    else:
        print("NO")

    # 如果表达式要重复使用,可用预编译的方式减少再编译的时间,提高效率
    pattern = re.compile(r'(\d+)/(\d+)/(\d+)') # 使用正则括号分组,常见于爬虫中的字段获取
    m = pattern.match(text1)
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))
    print(m.group(4)) # 分组越界将会出现 IndexError

def _25():
    '''
    字符串搜索与替换
    '''
    import re
    text = "2017-12-11"

    pattern = re.compile(r'(\d+)-(\d+)-(\d+)')  
    print(pattern.sub(r'\3/\2/\1',text)) # 分组替换

    # 使用回调函数进行定制替换
    def formatDate(m):
        from calendar import month_abbr
        month = month_abbr[int(m.group(2))]
        year = m.group(1)[2:]
        return "{}-{}-{}".format(m.group(3),month,year)

    print(pattern.sub(formatDate,text))

def _27():
    '''
    字符串最短匹配 -- 使用正则非贪婪模式
    这一节展示了在写包含点(.)字符的正则表达式的时候遇到的一些常见问题。 在一个模式字符串中，点(.)匹配除了换行外的任何字符。 然而，如果你将点(.)号放在开始与结束符(比如引号)之间的时候，那么匹配操作会查找符合模式的最长可能匹配。 这样通常会导致很多中间的被开始与结束符包含的文本被忽略掉，并最终被包含在匹配结果字符串中返回。 通过在 * 或者 + 这样的操作符后面添加一个 ? 可以强制匹配算法改成寻找最短的可能匹配。
    '''

    import re
    pattern = re.compile(r'\"(.*?)\"')
    text = 'D.Wade said "this is my horse !" James replied , "Yes it is!" ' 
    print(pattern.findall(text))

def _28():
    '''
    多行字符串匹配
    '''
    import re
    pattern = re.compile(r'/\*((?:.|\n)*?)\*/')
    textlines = """/* comment 1
    comment 2
    comment 3
    */
    """
    print(pattern.findall(textlines))

if __name__ == '__main__':
    _28()