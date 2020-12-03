#!/usr/bin/env python3
# coding: utf8

# %matplotlib inline

import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    # plt.ion()
    x = np.linspace(0, 2, 100)

    plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
    plt.plot(x, x ** 2, label='quadratic')  # etc.
    plt.plot(x, x ** 3, label='cubic')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.title("Simple Plot")
    plt.legend()

    plt.show()
