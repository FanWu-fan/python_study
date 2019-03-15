# def echo(message):
#     print(message)

# schedule = [(echo,"SPAM!"),(echo,'Ham!')]
# for (func,arg) in schedule:
#     func(arg)


#######################################
#计算一个嵌套的子列表结构中所有数字的总和:
#[1,[2,[3,4],5],6,[7,8]]


# def sumtree(L):
#     tot = 0
#     for x in L:
#         #isinstance(obj,class)判断obj是不是class的实例化
#         #isisntance(1,int)->True
#         print("x:",x)
#         if not isinstance(x,list):
#             tot += x
#         else:
#             tot += sumtree(x)
#     return tot
# L=[1,[2,[3,4],5],6,[7,8]]
# print(sumtree(L))


########################################################

# def knights():
#     title = "Sir"
#     action = (lambda x: title + ' ' + x)
#     return action
# act = knights()
# print(act('robin'))


########################################################
# L = [
#     lambda x: x**2,
#     lambda x: x**3,
#     lambda x: x**4
# ]
# for f in L:
#     print(f)
#     print(f(2))
# #OutPut: 4 8 16
# print(L[0](3))
# #OutPut:9
####################################################