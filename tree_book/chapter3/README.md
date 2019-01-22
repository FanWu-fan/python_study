# Chapter3-迭代器和解析
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
