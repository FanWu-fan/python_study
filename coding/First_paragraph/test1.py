def get():
    file = open('./1.txt', 'r')
    averages = {}
    name = None
    for line in file:
        line = line.strip()
        if line == '':
            continue
        if line.endswith(':'):
            if name is not None:
                averages[name] = total/num
            name = line[:-1].strip()
            num = 0
            total = 0
        else:
            num += 1
            total += float(line)
    file.close()
    return averages


class A:
    def __init__(self, x):
        print("A-->init x")
        self.x = x

    def f(self, x):
        print('A-->f')
        return self.g(x) - 1

    def g(self, x):
        print('A-->g')
        return 2*x


class B(A):
    def g(self, y):
        print('B-->g')
        return self.x + y


class C(B):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def f(self, x):
        return self.x + self.y


class D(B):
    def __init__(self, x, y):
        super().__init__(x)
        self.x += y
        self.y = y

    def g(self, y):
        return self.y + y

    def f(self, x):
        return super().f(x) - x


if __name__ == '__main__':
   # a = A(3)
   # b = B(2)
    #c = C(2, 4)
    d = D(1, 3)
    print(D.mro())
    # print(c.g(3))
    # print(b.f(3))
    print(d.f(2))