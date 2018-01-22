
# coding: utf-8

# In[5]:


from matplotlib import pyplot as plt
import pandas as pd 

species = pd.read_csv('species_info-Copy1.csv')
species.head()


# In[6]:


observations = pd.read_csv('observations-Copy1.csv')
observations.head(10)


# In[14]:


species_observations = pd.merge(species, observations)


# In[33]:


species_observations['is_protected'] = species_observations.conservation_status.notnull() 

species_observations.head()


# In[65]:


spec_ob_group= species_observations[['category','scientific_name','is_protected','park_name','observations']]

spec_ob_group.head()


# In[78]:


s_o_protected= spec_ob_group[(spec_ob_group.is_protected == True) & (spec_ob_group.category != 'Vascular Plant') & (spec_ob_group.category !='Nonvascular Plant') ]

s_o_protected



# In[79]:


s_o_protected= s_o_protected.groupby(['category','park_name']).observations.sum().reset_index().sort_values(by='park_name')
s_o_protected


# In[72]:


s_o_pro_pivot = s_o_protected.pivot(index='category',columns='park_name',values='observations')
s_o_pro_pivot.columns = ['Bryce National Park','Great Smoky Mountains National Park','Yellowstone National Park','Yosemite National Park']
s_o_pro_pivot

