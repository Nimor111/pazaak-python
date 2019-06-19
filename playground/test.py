class A:
    def __init__(self, a):
        self.a = a


def func(a: A):
    a.a += 1


def main():
    x = A(5)
    print(x.a)
    func(x)
    print(x.a)


if __name__ == "__main__":
    main()
