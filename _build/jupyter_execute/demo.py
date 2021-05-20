#!/usr/bin/env python
# coding: utf-8

# # Demo notebook

# We can also create parts of our Jupyter Book based on Jupyter Notebooks.

# Let's simulate data for two conditions and print their first ten rows:

# In[1]:


import numpy as np

cond_1 = np.random.rand(100)
print(f'Condition 1 = {cond_1[:10]}')

cond_2 = cond_1 + (np.random.rand(100))
print(f'Condition 2 = {cond_2[:10]}')


# We can also display in our Jupyter Book more complex datastructures, like pandas dataframes:

# In[2]:


import pandas as pd

df = pd.DataFrame(
    {'condition_1': cond_1, 'condition_2': cond_2}, 
    index=np.arange(100)
)

df[:10]


# And of course, we can display plots as well!

# In[3]:


import matplotlib.pyplot as plt

plt.scatter(cond_1, cond_2, alpha=.6)
plt.xlabel('condition 1')
plt.ylabel('condition 2')
plt.title('Scatterplot')
plt.show()

