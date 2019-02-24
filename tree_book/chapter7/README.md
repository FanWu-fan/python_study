# Chapter7 函数的高级话题
开始使用函数时，开始面对如何将组件聚合再一起的选择，如何将任务分解成为更有针对性的函数（导致了聚合性），函数如何通行（耦合性）等。
* 耦合性：对于输入使用参数并且对于输出使用 **return** 语句。
* 耦合性：只有在真正必要的情况下使用 **全局变量**。
* 耦合性：不要改变 **可变类型** 的参数。
* 聚合性：每个函数都应该有一个单一的，统一的目标。
* 耦合：避免直接改变在另外一个模块文件中的变量。

## 递归计算
计算一个嵌套的子列表结构中所有数字的总和:
[1,[2,[3,4],5],6,[7,8]]
```python
def sumtree(L):
    tot = 0
    for x in L:
        #isinstance(obj,class)判断obj是不是class的实例化
        #isisntance(1,int)->True
        if not isinstance(x,list):
            tot += x
        else:
            tot += sumtree(x)
    return tot
L=[1,[2,[3,4],5],6,[7,8]]
print(sumtree(L))
```
## 间接函数的调用
由于pyhton函数是对象，因此函数对象可以赋值给其他的名字，传递给其他的函数，嵌入到数据结构中，还可以由一个函数表达式后面的括号中的列表参数调用。
```python 
def echo(message):
    print(message)

schedule = [(echo,"SPAM!"),(echo,'Ham!')]
for (func,arg) in schedule:
    func(arg)
    
'''
SPAM!
Ham!
'''
```
## 匿名函数：lambda
* lambda 是一个表达式，而不是语句
* lambda 的主体是一个单个的表达式，而不是一个代码块
* *lambda arguement1, arguement2, arguementN: expression using arguement*
```python
f = lambda x,y,z: x+y+z
f(2,3,4)
#Output: 9

x = 
```


