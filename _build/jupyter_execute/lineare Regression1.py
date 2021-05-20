#!/usr/bin/env python
# coding: utf-8

# # Lineare Regression (manuell)

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


def f(a, x):
    return a * x


def J(a, x, y):
    return (y - a * x) ** 2


def J_ableitung_a(a, x, y):
    return -2 * x * (y - a * x)


# In[3]:


point = (1, 4)
lr = 0.05
a = 1
for i in range(0, 20):
    da = J_ableitung_a(a, point[0], point[1])
    a = a - lr * da
    print("Kosten J = " + str(round(J(a, point[0], point[1]),3)) + " wenn a = " + str(round(a,3)))

    xs = np.arange(-2, 2, 0.1)
    ys = f(a, xs)
    plt.plot(xs, ys)

plt.scatter(point[0], point[1])
plt.show()


# In[ ]:




