# Chapter5-函数
1. 举例  

|语句 | 例子|  
|:--:|:--:|
calls|myfunc("spam","eggs",meat = ham)
def | def adder(a,b=1,*c)
return | return a+b+c[0]
global | def changer(): global x ; x = 'new'
nonlocal | def changer(): nonlocal x; x = 'new'
yield |def squares(x): for i in range(x): yield i **2
lambda | Funcs = [lambda x: x** 2,lambda x: x*3]

2. 函数只是一个对象，在运行时，创建一个新的函数名并将其赋值给一个变量名。
```python
if test :
    def func():
        ...
else:
    def func():
        ...
func() #python在程序运行前不需要全部定义
othername() = func() #可以调用
func.attr = value #可以将任意的属性附加到记录信息
```
3. 作用域  
对于一个“def”语句：  
* 变量名引用分为三个作用域进行查找LEGB：首先是本地(L)-->函数内(E)-->全局(G)-->内置(B)
* 默认情况下，变量名赋值会创建或者改变本地变量
* 全局声明和非本地声明将赋值的变量名映射到模块文件内部的作用域

4. 嵌套作用域和lamba
    lamba是一个表达式，将会生成后面调用的一个新的函数，与def语句很相似。由于它是一个表达式，尽管可以使用在def中不能使用的地方，但是lambda表达式引入了新的本地作用域。多亏了嵌套作用域查找层，以下代码才得以运行。
```python


```
