from w5 import spam


def f():
    print(x)


if __name__ == "__main__":
    x = 2

    f()
    spam.f()
    print(spam.x)
