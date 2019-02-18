# def func(spam,eggs,toast=0,ham=0):
#     print((spam,eggs,toast,ham))

# func(1,2)   # Output: (1,2,0,0)
# func(1,ham=1,eggs=0)  # Output: (1,0,0,1)
# func(spam=1,eggs=0)  # Output: (1,0,0,0)
# func(toast=1,eggs=0,spam=3)  # Output: (3,0,1,0)
# func(1,2,3,4)    # Output: (1,2,3,4)

'''
min调用的实例
'''
def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res

def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first  = arg
    return first

def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]

def minmax(test,*args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res
def lessthan(x,y): return x < y
def grtrthan(x,y): return x > y

# print(minmax(lessthan,4,2,1,5,6,3))
# print(minmax(grtrthan,4,2,1,5,6,3))

def intersect(*args):
    res = []
    print(args)
    for x in args[0]:
        print('x:',x)
        for other in args[1:]:
            print('other:',other)
            if x not in other: pass
            else :
                res.append(x)
                print('res:',res)
    return print(res)

def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return print(res)

s1, s2, s3 = 'SPAMH', 'SCAM', 'SLAMH'
# intersect(s1,s2,s3)
# union(s1,s2)

'''
练习题
'''
def func(a,**kargs):
    print(a,kargs)
func(a=1,c=3,b=2)