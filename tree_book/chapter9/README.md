# Chapter9 类和OOP
![](picture/2019-03-18-20-50-25.png)
类的继承，类树，低端有两个实例(l1,l2),在它上有个类(c1),而顶端有两个超类/基类(c2和c3)。继承就是由下至上搜索此树，来寻找属性名称所出现的最低的地方。
* I1.x 和 I2.x 两者都会在 C1 中找到 x 并停止搜索，因为 c1 比 c2 位置低。
* I1.y 和 I2.y 两者都会在 C1 中找到 x 并停止搜索，因为 y只出现在c1中。 
* I1.z 和 I2.z 两者都会在 C2 中找到 z 并停止搜索, 因为 c2 比 c3 更靠左侧。

以双下划线命名的方法(\_\_x\_\_)是特殊的钩子：
* 当新的实例构造时，会调用\_\_x\_\_
* 当实例出现在 + 表达式时，会调用\_\_add\_\_
* 当打印一个对象的时候，运行\_\_str\_\_

```python
class FirstClass(object):
    def setdata(self,value):
        self.data = value
    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def __init__(self,value):
        self.data = value
    def __add__(self,other):
        return SecondClass(self.data + other)
    def __str__(self):
        return 'hello：%s'%self.data


y = SecondClass('adc') 
y.display() #adc
print(y)    #hello：adc 直接调用 __str__
b = y + 'xyz'   #使用+号时，直接调用 __add__
b.display()     #adcxyz
```
