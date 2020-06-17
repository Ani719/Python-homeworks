class A:

    def init(self, a):
        self.a = a


    def add(self, b):
        return self.a + b.a


a1 = A(5)
a2 = A(3)
a3 = a1 + a2
print(a3)

a4 = A('Ani')
a5 = A('Ararat')
a6 = a4 + a5
print(a6)