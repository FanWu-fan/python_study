# class C:
#     @staticmethod
#     def meth():
#         pass

# class C：
#     def meth():
#         pass
#     meth = staticmethod(meth)

###############################################################
# class Spam:
#     numInstances = 0
#     def __init__(self):
#         Spam.numInstances = Spam.numInstances +1
    
#     @staticmethod
#     def printNumInstances():
#         print("Number of instances: ",Spam.numInstances)

# a= Spam()
# b = Spam()
# c = Spam()
# Spam.printNumInstances()
# a.printNumInstances()

#######################################################################
# class tracer:
#     def __init__(self,func):
#         self.calls = 0
#         self.func = func
#         print("my name :", self.func.__name__)
#     def __call__(self,*args):
#         self.calls +=1
#         print('call %s to %s'%(self.calls,self.func.__name__))
#         self.func(*args)
    
# #和语句一样：spam = tracer(spam),然后调用__init__函数和__call__
# @tracer
# def spam(a,b,c):    
#     print(a,b,c)


# spam(1,2,3)
# spam('a','b','c')
# spam(4,5,6)    

# # my name : spam
# # call 1 to spam
# # 1 2 3
# # call 2 to spam
# # a b c
# # call 3 to spam
# # 4 5 6
#####################################################################
def decorator(aClass)：
