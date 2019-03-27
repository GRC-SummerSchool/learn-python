import numpy as np
import random

display_w = 800
display_h = 600
w = display_w / 2
np.random.seed(1234)

def f1(x):
    x = (x - w) / w
    y = 0.25 * display_h * np.sin(np.pi * x) + 200
    y = y * (1 + noise(x))

    return y

def f2(x):
    x = (x - w) / w
    y = 0.75 * display_h * x ** 3 + 300
    y = y * (1 + noise(x))

    return y

def f3(x):
    x = (x - w) / w
    y = 0.5 * display_h * (1 / (1 + np.exp(-20 * x))) + 100
    y = y * (1 + noise(x))

    return y

def f4(x):
    x = (x - w) / w + 1
    y = 0.5 * display_h * np.sqrt(x) + 100
    y = y * (1 + noise(x))

    return y

def noise(arr):

    err = np.random.normal(0.1,0.05,arr.shape[0])

    for idx, val in enumerate(err):
        if random.random() < 0.5:
            p_m = 1
        else:
            p_m = -1

        err[idx] = p_m * val

    return err