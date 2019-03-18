###########################################################
# def gensquares(N):
#     for i in range(N):
#         yield i**2

# for i in gensquares(5):
#     print(i,end=':')
# #OutPut: 0:1:4:9:16:
# x = gensquares(4)
# print(x)
# #<generator object gensquares at 0x000001E470055888>
# #得到的是一个生成器对象，支持迭代协议，生成器对象有一个__next__方法，它可以
# #开始这个函数，或者从它上次yield值后的地方恢复，并且在得到一系列的值的最后一个时，
# #产生StopIteration异常，next(x)内置函数为我们调用了一个对象的X.__next__()方法
# print(next(x)) #0
# print(next(x)) #1
# print(next(x)) #2
# print(next(x)) #9
# print(next(x)) #StopIteration

###########################################################
X = 100
def p():
    import __main__
    print(__main__.X)
    X=33
p()

