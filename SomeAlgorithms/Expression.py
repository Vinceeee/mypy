#coding=utf-8
#! usr/bin/python

# 定义枚举方法
def enum(**enums):
    return type('Enum',(),enums)

class OprStack(object):

    def __init__(self):
        self.stack = list()

    def append(self,char):
        self.stack.append(char)

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
        return ""

    def __str__(self):
        return "%s" % (self.stack)

    def isEmpty(self):
        return (len(self.stack) == 0)

class ExpHandler(object):

    ExpStatus = enum(Normal=0, CharException=1 , ExpError=2 )
    ValidValue = "0123456789.+-*/()"

    def __init__(self):
        self.priority = 0
        self.expQueue = list()
        self.oprStack = OprStack()
        self.numStack = list()
        self.status = self.ExpStatus.Normal

    def readChar(self,char):
        if not self.varifyChar(char):
            self.status = self.ExpStatus.CharException
            return 1

        curPriority = self.charHandle(char)
        if curPriority == 0:
            self.numStack.append(char)
        else:
            if len(self.numStack) != 0:
                num = int("".join(self.numStack))
                self.numStack = list()
                self.expQueue.append(num)

            while self.priority > curPriority:
                if self.priority == 4 :
                    break;
                opr = self.oprStack.pop()
                if opr != "(":
                    self.expQueue.append(opr)
                self.priority = self.charHandle(opr)

            if curPriority != 1:
                self.oprStack.append(char)
                self.priority = curPriority


    def varifyChar(self,char):
        if char not in self.ValidValue:
            return False
        return True

    def charHandle(self,char):
        if char in ")" :
            return 1
        elif char in "+-" :
            return 2
        elif char in "*/" :
            return 3
        elif char in "(" :
            return 4
        else :
            return 0

    def attachOprStack(self):
        while not self.oprStack.isEmpty():
            self.expQueue.append(self.oprStack.pop())

    def calculate(self):
        tmpStack = list()
        for each in self.expQueue:
            if isinstance(each,int):
                tmpStack.append(each)
            else:
                num2 = tmpStack.pop()
                num1 = tmpStack.pop()
                result = 0
                exp = "result = %s %s %s " % (num1,each,num2)
                exec(exp)
                tmpStack.append(result)

        print "result is %s " % (tmpStack)

# (7) 主程序
if __name__ == '__main__':

    exp = "(12+2)+3*44/(3+4)"
    handler = ExpHandler()
    # print "handler status : %s " % (handler.status)
    for seq,eachchar in enumerate(exp):
        print "%s: %s " % (seq,eachchar)
        handler.readChar(eachchar)
        if handler.status != handler.ExpStatus.Normal:
            print "Expression Exception : %s ! '%s' is invalid character " % (exp , eachchar)
            break

    handler.attachOprStack()

    handler.calculate()
