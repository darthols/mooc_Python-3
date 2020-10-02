#!/usr/bin/env python3
# coding: utf8


def div(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("attention /0")
    except TypeError:
        print("faut de nombres")
    print("continuons")


if __name__ == "__main__":
    div(1, "0")
