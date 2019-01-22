# Chapter3 迭代器和解析
1. 利用迭代特性读文件：
```python
with open('1.txt','r') as f:
    for (n,line) in enumerate(f):
        print(n,line,end ='')
#没有读文件，让for循环在每轮自动调用next从而前进到下一行
#用“end= ''”来防止输出变成两行隔开
#由于print在输出的时候会自带换行符，因此要用end指定print输出自带不是换行
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
3. 列表生成式(二维列表),利用列表生成式产生二维列表
```python
>>>[[0 for col in range(5)] for row in range(4)]
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

>>>[[col for col in range(5)] for row in range(4)]
[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]

>>>[[row for col in range(5)] for row in range(4)]
[[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3]]

>>> s = [[1.2,2.3],[3.4,4.5]]
>>>[[int(m) for m in i] for i in s]
[[1, 2], [3, 4]]
```