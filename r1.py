
def myfind(x,y):                                            #查找字符串中某个字符出现的有所索引
    return [a for a in range(len(y)) if y[a]==x]


def Existence_operation(index1,index2) :                    #判断两个位置之间是否存在运算
     pass


print("输入代数式")
Alge_expre=input("代数式->")
Alge_expre_length=len(Alge_expre)
print(Alge_expre_length)
y=Alge_expre[0:1]
if '(' or ')' in Alge_expre:                              #判断括号存在情况，两个列表对称位置构成一对括号
    a_index=myfind('(',Alge_expre)
    b_index=myfind(')',Alge_expre)









print(a_index,b_index)
equalsign=Alge_expre[1:2]
print(Alge_expre)
print(y)
print(equalsign)







