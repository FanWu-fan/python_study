# Chapter8 迭代和解析，第二部分
## 列表解析和map
pyhton内置函数 ord 函数会返回一个单字符的ASCII整数编码：
> ord('s')
> 115
> 
采用for循环
```python
res = []
for x in 'SAPM':
    res.append(ord(x))
```
采用map
```python
list(map((lambda x:ord(x)),"SPAM"))
list(map(ord,"SPAM"))
```
采用列表解析式
```python
res = [ord(x) for x in "spam"]
```
实际上，列表解析还能够更加通用，你可以在一个列表解析中编写任意数量的嵌套for循环，并且每一个都有可选的关联if的测试。
```python
[expression for target1 in iterable1 [if condition1]
            for target2 in iterable2 [if condition2]
            for target3 in iterable3 [if condition3]...]

[x+y for x in [0,1,2] for y in [100,200,300]]
#OutPut:[100, 200, 300, 101, 201, 301, 102, 202, 302]
```
## 列表解析和矩阵
```python
M=[[1,2,3],
    [4,5,6],
    [7,8,9]]
N=[[2,2,2],
    [3,3,3],
    [4,4,4]]

#提取某一行的元素
[row[1] for row in M]
#Out: [2, 5, 8]

#提取对角线
[M[i][i] for i in range(len(M))]

#矩阵每个元素相乘
[M[row][col] * N[row][col] for row in range(3) for col in range(3)]
# Out: [2, 4, 6, 12, 15, 18, 28, 32, 36]

#两层循环，外面一层是 row
[[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]
# Out: [[2, 4, 6], [12, 15, 18], [28, 32, 36]]
```
## 理解列表解析式
map调用比for循环快两倍，而列表解析往往比map调用稍快一些。速度的差距来自于底层，map和列表解析是在解释器中以C语言的速度来运行，比Python的for循环代码在PVM中步进运行快很多。。

### 重访迭代器：生成器
如今Python对延迟提供更多的支持--它提供了工具在 **需要** 的时候才 **产生结果**，而不是立即产生结果。特别地，有两种语言结构京可能地延迟结果创建。
* **生成器函数**：编写为常规的 **def** 语句，但是使用 **yield** 语句 **一次** 返回 **一个** 结果，在每个结果之间 **挂起** 和继续它们的状态。
* 生成器表达式类似于上一小节的 **列表解析式**，但是，他们返回按需产生结果的一个 **对象**，而不是构建一个结果列表。

由于二者都 **不会一次性** 构建一个列表，它们 **节省了内存空间**，并且允许计算时间 **分散** 到各个结果请求。

### 生成器函数： yield VS return
* 常规函数：接受输入参数并 **立即** 送回单个结果。
* 生成器函数：送回一个值并随后从其退出的地方继续的函数，它们随时间产生值的一个序列

#### 状态挂起
和返回一个值并 **退出** 的 **常规函数** 不同，**生成器函数** 自动在生成值的时刻 **挂起** 并继续函数的执行。因此，他们对于提前计算整个一系列值以及在类中手动保存和恢复状态都很有用，由于生成器函数在挂起时保存的状态包含它们的整个本地作用域，当函数恢复时，它们的本地变量保持了信息并且使其可用。

生成器函数和常规函数之间的主要的代码不同之处在于，生成器 **yields** 一个值，而不是 **返回** 一个值。 yield语句挂起该函数并向调用者发送回一个值，但是，保留足够的状态以使得 **函数能够从它离开的地方继续。** 当继续时，函数在上一个 **yield**返回后立即继续执行。从函数的角度来看，这允许其代码随着时间产生一系列的值，而 **不是一次计算** 它们并在诸如 **列表** 的内容中送回它们。

#### 迭代协议整合
可迭代的对象定义了一个 **\_\_next\_\_** 方法，它要么返回迭代中的下一项，或者引发一个特殊的 **StopInteration** 异常来终止迭代。一个对象的迭代器用 **iter** 内置函数来接收。

直接效果就是生成器函数，编写为包含yield语句的def语句，自动地支持迭代协议，并且由此可能用在任何迭代环境中以随着时间并根据需要产生结果。

### 生成器函数应用
```python
def gensquares(N):
    for i in range(N):
        yield i**2

for i in gensquares(5):
    print(i,end=':')
#OutPut: 0:1:4:9:16:
x = gensquares(4)
print(x)
#<generator object gensquares at 0x000001E470055888>
#得到的是一个生成器对象，支持迭代协议，生成器对象有一个__next__方法，它可以
#开始这个函数，或者从它上次yield值后的地方恢复，并且在得到一系列的值的最后一个时，
#产生StopIteration异常，next(x)内置函数为我们调用了一个对象的X.__next__()方法
print(next(x)) #0
print(next(x)) #1
print(next(x)) #2
print(next(x)) #9
print(next(x)) #StopIteration
```
for循环(以及其他的迭代环境)以同样的方式与生成器一起工作：通过重复调用**\_\_next\_\_**,直到捕获到一个异常。

## 生成器表达式：迭代器遇到列表解析
编写一个 列表解析 基本等同于：**在一个list内置调用中包含一个生成器表达式以强迫其一次生成列表中所有的结果**。
```python
[x**2 for x in range(4)]
# Out: [0, 1, 4, 9]

(x**2 for x in range(4))
# <generator object <genexpr> at 0x000001B9F0DB59E8>

G = (x**2 for x in range(4))
next(G) #0
next(G) #1
next(G) #4
next(G) #9
next(G) #StopInteration
```
生成器函数表达式大体上可以认为是对 **内存空间**的优化，它们不需要像方括号的列表解析式一样，一次构建出 **整个结果列表**。

## 生成器函数 VS 生成器表达式
同样的迭代可以用 **生成器函数** 或 **一个生成器表达式** 编写。
```python
G = (c*4 for c in "SPAM")
list(G)
# ['SSSS', 'PPPP', 'AAAA', 'MMMM']

def timefour(S):
    for c in S:
        yield c*4
G = timefour('spam')
list(G)
# ['ssss', 'pppp', 'aaaa', 'mmmm']

```

### 生成器是单迭代对象
生成器函数和生成器表达式自身都是迭代器，并且支持 **一次**活跃迭代，实际上，一个生成器的迭代器是生成器自身。
```python
G = (c*4 for c in 'SPAM')
iter(G) is G
# True
T1 = iter(G)
next(T1) # 'SSSS'
next(T1) # 'PPPP'

T2 = iter(G)
next(T2) # 'AAAA'
next(T2) # 'MMMM'

#这个时候再通过给G赋新值都是无用的，因为已经迭代完毕,只能重新赋值
T3 =  (c*4 for c in 'SPAM')
```
这个与内置的类型是不同的，它们支持多个迭代器并且在一个活动迭代器中传递并反应它们在原处的修改。
```python
L = [1,2,3,4]
I1,I2 = iter(L),iter(L)
next(I1) #1
next(I1) #2
next(I1) #3

next(I2) #1
next(I2) #2
next(I2) #3
```
## 函数陷阱
### 本地变量是静态检测的
python定义的在一个函数中进行分配的变量名是默认为 **本地变量** 的，它们存在于函数的作用域并只在函数运行时存在。python是 **静态检测** python的本地变量的，当编译def代码时，不是通过发现赋值语句在运行时进行检测的。
一般来说，没有在函数中赋值的变量名会在整个模块文件中查找。
```python
X = 99
def p():
    print(X)
P() # 99


def p2():
    print(X)
    X = 88
p2() #UnboundLocalError: local variable 'X' referenced before assignment
```
在编译时，python看到了对X的赋值语句，并且决定了X将会在函数中任一地方都将是 **本地变量名**，但是，在函数实际运行时，因为在print执行时赋值语句并没有发生，python告诉你正在使用一个未定义的变量名。实际上，任何在函数体内的赋值都会将其成为一个本地变量名。Import、=、嵌套def、嵌套类等，都会受这种行为的影响。
```python
#下面这种用法是错误的
X=100
def p():
    global X
    print(X)
    X=88
---------------------------------------------
#应该导入 __mian__模块,从__main__命名空间得到了全局变量版本的X
X = 100
def p():
    import __main__
    print(__main__.X)
    X=33
p()

```

