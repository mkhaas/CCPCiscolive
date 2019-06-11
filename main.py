#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Ciscolive - Simple example to demo CCP GPU.  


# In[19]:


from __future__ import absolute_import, division, print_function, unicode_literals
import os
import tensorflow as tf
import numpy as np
from tensorflow import keras

tf.__version__


# In[20]:


model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])


# In[21]:


model.compile(optimizer='sgd', loss='mean_squared_error')


# In[22]:


xs = np.array([-1.0,  0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)


# In[23]:


model.fit(xs, ys, epochs=500)


# In[24]:


print(model.predict([10.0]))


# In[25]:


print('\ntrain_labels.shape: {}, of {}'.format(xs, xs.dtype))
print('test_labels.shape: {}, of {}'.format(ys.shape, ys.dtype))
print(model.inputs)
print(model.outputs)
inputs={'xs': model.input}
print(inputs)
outputs={t.name:t for t in model.outputs}
print(outputs)


# In[26]:


import tempfile
import sys

#MODEL_DIR = tempfile.gettempdir()
MODEL_DIR = "/home/jovyan/data-vol-1"
version = 1
export_path = os.path.join(MODEL_DIR, str(version))
print('export_path = {}\n'.format(export_path))
if os.path.isdir(export_path):
  print('\nAlready saved a model, cleaning up\n')
  get_ipython().system('rm -r {export_path}')
  


# In[27]:


export_path


# In[28]:


tf.saved_model.simple_save(
  keras.backend.get_session(),
   export_path,
   inputs={'xs': model.input},
  outputs={t.name:t for t in model.outputs})


# In[29]:



print('\nSaved model:')
#get_ipython().system('ls -l {export_path}')


# In[ ]:




