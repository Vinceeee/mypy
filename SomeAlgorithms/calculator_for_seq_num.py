# coding=utf-8
# 上句为设定文本编码为utf-8

#等比数列求和
def SumOfDengBi(a1,q,n):
    sum = 0.0
    if ( n == 1 ):
        return a1
    if ( q == 1 ):
        return a1*n
    sum = a1*(1-(q**(n+1)))/(1-q)
    return sum

#main
a1 = input("请输入首项： ")
q  = input("请输入公比： ")
n  = input("请输入项数： ")
Sum = SumOfDengBi(a1,q,n)
print Sum
