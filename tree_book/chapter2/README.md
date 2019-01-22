# Chapter2 序列解包
1. 扩展的序列解包语法：
>a, *b = seq(seq = [1,2,3,4]) -> a=1,b=[2,3,4]
>a,*b = 'spam' --> a= 's',b = ['p','a','m']  
>和切片不同的是，用序列解包，返回的都是列表。而切片返回同类型的序列
```python
L = list(range(4))
whlie L:
    front,*L= L
    print(front, L)
>>>0 [1,2,3]
>>>1 [2,3]
>>>2 [3]
>>>3 []
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
   > **list** (range(5)), list(range(2,5)), list(range(0,10,2))可以查看range()产生的列表  
   >使用range遍历字符串跳过元素：  
   >s = 'abcdefghijk'
   >for i in range(0,len(s),2):print(s[i], end=' ')

>然而上述方法使用的并不多，一般常用为：
>for c in s[::2]: print(c,end = ' ')

>L= [1,2,3,4,5]  改变列表内的每一个值正确做法，这里是在原处修改，所有 **共享引用** 都会发生变化
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

6. enumerate枚举，在迭代协议中，产生一个 **迭代次数n**  
```python
S = 'spam'
for (n,s) in enumerate(s):
    print(n,s)
--> 0 s
--> 1 p
--> 2 a 
--> 3 m
```
