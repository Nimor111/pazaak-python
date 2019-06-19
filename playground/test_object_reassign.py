class A:
    def __init__(self, a):
        self.a = a


a = A(0)
b = a
print(b.a)
b = A(5)

print(a.a)
print(b.a)
