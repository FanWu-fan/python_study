# 一。对象
1. 判断一个字符串的数字部分(列表解析）：  
```python
s = 'total executian tima: 12 s'  
[t.isdigit() for t in s.split() ]  
```
>  isdigit字符串只包含数字返回TURE，不包括小数点  

>读文件readline**s**会产生一个列表将文件整个读入内存中：
```python
lines = open('1.txt').readlines()
lines = [line.rstrip() for line in lines]
```
2. 字符串支持格式化的高级替代操作：
> '%s,eggs,and %s'%('spam','SPAM!')
> >'spam,eggs,and SPAM!'  
> 
> '{0}, eggs,and {1}'.format('spam','SPAM!')
> >'spam, eggs,and SPAM!'

3. 在 import 一个 A.py 文件以后,使用**dir(A)**获得模块内部的可用的变量名的列表。其中以双下划线开头并结尾的变量名，为python预定义的内置变量名。
>['\_\_builtins__',
 '\_\_cached__',
 '\_\_doc__',
 '\_\_file__',
 '\_\_loader__',
 '\_\_name__',
 '\_\_package__',
 '\_\_spec__',
 ]
> * \_\_builtins__:内建模块
> * \_\_cached__:python的缓存
> * \_\_doc__:帮助文档
> * \_\_file__:python文件绝对位置

4. 利用help()生成交互界面的帮助  
   利用help(str.center)查询特定的方法调用。

5. *x is y* OR *x is not y*  
   验证x和y在内存地址上是否严格相等 

6. 在python中，变量并不需要预声明，但是在使用之前，至少要赋一次值。实际上，这意味着在对其进行加法计算时要计数器初始化为0，在列表后添加元素前，要首先初始化列表为一个空列表。
   
7. "//"截断除法：  
   5 / 2 --> 2.5  
   5 // 2 --> 2
   5 // -2 --> -3

8. 小数、分数、浮点数：  
   ```python
   0.1 + 0.1 + 0.1 - 0.3 --> 5.5511...7e-17
   >>> from fractions import Fraction
   >>> Fraction(1,10) + Fraction(1,10) + Fraction(1,10) - Fraction(3,10)
   Fraction(0,1)  

   >>> from decimal import Decimal
   >>> Decimal('0.1') +   Decimal('0.1') + Decimal('0.1') -  Decimal('0.3')
   >>>  Decimal('0.0')
   ```

9. 变量（变量名）没有类型，只有对象才有类型。比如：a = 3，a是变量，a引用整数对象3.每一个对象都包含一个头部信息（标记了这个对象的类型），以及一个引用计数器。

10. 共享引用。如果是可变对象：**列表** 会原处修改值，改变所有变量。  
    如果不是可变对象：*字典、数值、字符串*，则不影响。
```python
使用共享应用时，相互影响
L1 = [1, 2, 3]
L2 = L1
>>> L1.append(4)
>>> L2 --> [1,2,3,4]
>>> L1 = 5
>>> L2 -->[1,2,3,4]
只有拷贝时，不影响
L1 = [1,2,3]
L2 = L1[:]
```
11. 打开文件时，使用R/r关闭转义字符的功能：
>    myfile = open(**r**'C:\new\text.dat','w')  
> 模式选择有两种：‘r’输入打开文件（默认）   
> ‘w'输出生成并打开文件,**会清空文件**   
> ’a'表示为在文件尾部追加内容而打开文件

12. 文本写入只能写入字符串，必须使用转换工具将对象转成字符串
> F.write(str(L) + str(D))  
在用* for line in file:*后。需要对每一行去除‘\n’.使用”line.rstrip()“-->PS:有时候使用line[:-1],可是一般最后一行没有‘\n’  
>>读取文件后将字符串还原：line.strip()  

>>将 （12， 13， 14）元组还原:首先将”字符串“切分为列  
>>list=line.splie(',')-->再将列表字符迭代为数字：[int(p) for p in list]注意这里int(‘34\n')=34  

>> 将读取的字符串"\[1,2,3,\]{'a':1,'b':2}\n"还原为：列表和字典  
>> 使用”eval"函数，将字符串当作可执行程序代码（含有python表达式的字符串），可以在脚本中使用,注意eval的字符串中不能使用“=” 。意味着不能赋值 
>>part = line.split('$')
>>obj = [eval(p) for p in part]  

13. 鉴于"eval"使用有风险（可能执行删库跑路代码），使用“pickle” 

## 总结    
1. 可变对象|不可变对象  
    :---:  |:---:  
      列表 | 字符串
      字典 | 元组  
      集合 | 数字 

2. 空的列表、元组、字典、字符串视为 False,常用用法“
> if X:-->if not X:  

3. 修改元组值：
> a = (1,2,3) --> (4,2,3)
> 利用切片：a = (4,) + a[1:]~~这里注意的是（4，）是元组，而（4）是数字”int“  




---
# 二。
1. 扩展的序列解包语法：
>a, *b = seq(seq = [1,2,3,4]) --> a=1,b=[2,3,4]
>a,*b = 'spam' --> a= 's',b = ['p','a','m']  
>和切片不同的是，用序列解包，返回的都是列表。而切片返回同类型的序列
```python
L = [1,2,3,4]
whlie L:
    front,*L= L
    print(front, L)
>>>1 [2,3,4]
>>>2 [3,4]
>>>3 [4]
>>>4 []
```
2. python没有swith以及case语句，可以根据变量选择动作，一般使用如下：  
```python
if:
elif:
else:
或则对字典进行索引运算或搜索列表：
choice = 'ham'
print({'spam':1.25
        'ham':1.99
        'eggs':0.99}[choice])

```
3. 执行简单的判断赋值：
> A = Y if X else Z

4. range循环计数器  
   range是通用的工具:
   >list(range(5)), list(range(2,5)), list(range(0,10,2))可以查看range()产生的列表  
   >使用range遍历字符串跳过元素：  
   >s = 'abcdefghijk'
   >for i in range(0,len(s),2):print(s[i], end=' ')

>然而上述方法使用的并不多，一般常用为：
>for c in s[::2]: print(c,end = ' ')

>L= [1,2,3,4,5]  改变列表内的每一个值正确做法，这里是在原处修改，所有共享引用都会发生变化
>for i in range(len(L)):  
>   L[i] += 1

>[x+1 for x in l]列表解析表达式，没有对最初的列表在原处修改，不会引起共享引用的变化

5. zip  
功能：产生元组,构造字典
```python
for (x,y) in zip(L1,L2):
    print(x,y,'--',x+y) #以两个列表同时循环

list(zip(L1,L2,L3))  #生成新的里列表

D = dict(zip(L1,L2))
```

6. enumerate枚举，在迭代协议中，产生一个迭代次数n  
```python
S = 'spam'
for (n,s) in enumerate(s):
    print(n,s)
--> 0 s
--> 1 p
--> 2 a 
--> 3 m
```

# 三。迭代器和解析
1. 利用迭代特性读文件：
```python
with open('1.txt','r') as f:
    for (n,line) in enumerate(f):
        print(n,line,end = '')
#没有读文件，让for循环在每轮自动调用next从而前进到下一行
#用“end= ''”来防止输出变成两行隔开
```
2. 利用列表解析：收集文件中特定字母开头的行
```python
lines=[line.rstrip() for line in open('1.txt') if line[0]=='p']

[x+y for x in 'abc' for y in 'lmn'] #列表解析式可以使用两个“for”
>> ['al','am','an','bl','bm','bn'......]

list(open('1.txt')) #利用每行迭代协议
tuple(open('1.txt'))
'&&'.join(open('1.txt')) #每行之间添加“&&”，输出一个长的字符串

a,b=open('data.txt')
a, *b = open('1.txt') #实际上open函数利用迭代返回每行的字符串列表


```
# 四。文档
1. python的文档资源 
 
    |形式|角色|  
    |:--:|:--:|
    #注释|文档中的文件
    dir函数 | 对象中可用属性的列表
    文档字符串：__doc\_\_ | 附加在对象上的文件中的文档
    help() |对象的交互帮助

2. 编写代码的陷阱：
   


