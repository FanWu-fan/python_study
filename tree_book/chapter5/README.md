# Chapter5 函数
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
* 变量名引用分为三个作用域进行查找 **LEGB** ：首先是本地(Local function)-->函数内(Enclosing function locals)-->全局(Global module)-->内置(Built-int python)
* 默认情况下，变量名赋值会创建或者改变本地变量
* 全局声明和非本地声明将赋值的变量名映射到模块文件内部的作用域

4. 嵌套作用域和lamba
    lamba是一个表达式，将会生成后面调用的一个新的函数，与def语句很相似。由于它是一个表达式，尽管可以使用在def中不能使用的地方，但是lambda表达式引入了新的本地作用域。

5.最小化文件修改
```python
#first.py
X = 99

#seconde.py
import first
print(first.X)
first.X = 88
```
第一个模块文件定义了变量X，这个变量在第二个文件中通过赋值被修改了，一个模块的全局变量一旦被导入就称成为了这个模块对象的一个属性。
这种方法可以跨文件修改变量，但是维护第一个模块时，很难知道会有模块修改X。
最好的解决办法时：在文件中通信最好的办法就是通过调用函数，传递参数，然后得到其返回值。
```python
#first.py
X = 99
def serX(new):
    global X
    X = new
# second.py
import first
first.setx(88)
```
当人们看到第一个模块时，会知道这是一个接入点，并且知道这将改变变量x，