'''
    python3 cookbook chap 2 strings
    http://python3-cookbook.readthedocs.io/zh_CN/latest/c02/p02_match_text_at_start_end.html
'''
def _211():
    '''
    去除字符串前后不必要的字符
    '''

    strings = "00000010000000"
    print(strings.lstrip('0'))
    print(strings.rstrip('0'))
    print(strings.strip('0'))

def _213():
    '''
    字符串对齐
    for more reference about string formatting in python : 
        https://docs.python.org/3/library/string.html#formatspec
    '''
    strings = "Thanks for using xxx"
    line1 = "1. Start Game"
    line2 = "2. Load  Game"

    print(format(strings,'>20')) # 左对齐
    print(format(line1,'>20')) # 左对齐
    print(format(line2,'>20')) # 左对齐

    print(format(strings,'<30')) # 右对齐
    print(format(line1,'<30')) # 右对齐
    print(format(line2,'<30')) # 右对齐

    print(format(strings,'^30')) # 居中对齐

    print(format(strings,'*^40')) #填充‘*’

    # 格式化多个值
    print(format("{:<30s}".format(strings),'>50')) 
    print(format("{:<30s}".format(line1),'>50')) 
    print(format("{:<30s}".format(line2),'>50')) 


    # 格式化输出固定长度的数字
    print(format(10.234,'0>8.2f')) # 字符长8位,保留两位小数,向前补零
    print(format(10.234,'0<8.2f')) # 字符长8位,向后补零,好像没什么意义

def _214():
    strings = ['I','E',"O","U"]
    print("".join(strings))

    # 使用生成器表达式合并字符串,提高效率
    strings = [123,'asdf',"UUUUU",10+67,(123,999)]
    print("-".join(str(each) for each in strings))

def _215():
    '''
    利用变量域格式化字符串
    '''

    name = "Stephen"
    age = 18

    print("{name} is {age} now".format_map(vars()))
    # print("{name} is {age} now,{date}".format_map(vars())) # It will be KeyError , 'date' is not found in vars()

def _216():
    '''
    长文本格式化输出
    '''
    textarea = """Wo cao!
    Why me again ? 我一个上海市长怎么就调到了党中央了？
    但是XP同志说，“中央已经决定了”
    当时我就念了两句诗：“
    苟。。。”
    """

    import textwrap
    import os

    tty_width = os.get_terminal_size().columns
    print(textwrap.fill(textarea,tty_width,initial_indent="    ",subsequent_indent="        "))

if __name__ == '__main__':
    _216()