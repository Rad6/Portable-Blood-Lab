class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def a(self):
        return self.__a
    @property
    def b(self):
        print("damn is b")
        return self.__b

    @a.setter
    def a(self, _a):
        print("set a is called")
        self.__a = _a
    
if __name__ == '__main__':
    t = A(1, 2)
    print(t.a, t.b)
    t.a = 84