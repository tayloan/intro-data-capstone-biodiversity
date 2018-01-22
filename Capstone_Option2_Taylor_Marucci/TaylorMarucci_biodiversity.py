

from matplotlib import pyplot as plt
import pandas as pd 

species1 = pd.read_csv('species_info-Copy1.csv')

species1.head()

species1.fillna('No Intervention',inplace = True)

protection_counts = species1.groupby('conservation_status').scientific_name.nunique().reset_index().sort_values(by='scientific_name')

plt.figure(figsize = (10,4))
ax = plt.subplot()
plt.bar(range(len(protection_counts)),protection_counts.scientific_name        .values)
ax.set_xticks(range(len(protection_counts)))
ax.set_xticklabels(protection_counts.conservation_status.values)
plt.ylabel('Number of Species')
plt.title('Conservation Status by Species')
plt.show()

species1['is_protected']= species1.conservation_status != 'No Intervention'
category_counts = species1.groupby(['category','is_protected']).scientific_name.nunique().reset_index()
category_pivot = category_counts.pivot(index = 'category', columns = 'is_protected',                                        values = 'scientific_name').reset_index()
category_pivot.columns = ['category','not_protected','protected']
category_pivot['percent_protected'] = category_pivot.protected / (category_pivot.protected + category_pivot.not_protected)

species1['is_protected']= species1.conservation_status != 'No Intervention'
category_counts = species1.groupby(['category','is_protected']).scientific_name.nunique().reset_index()
category_pivot = category_counts.pivot(index = 'category', columns = 'is_protected',                                        values = 'scientific_name').reset_index()
category_pivot.columns = ['category','not_protected','protected']
category_pivot['percent_protected'] = category_pivot.protected / (category_pivot.protected + category_pivot.not_protected)
category_pivot_sorted= category_pivot.sort_values(ascending = False,by='percent_protected').reset_index(drop=True)
category_pivot_sorted

animals_category=category_pivot_sorted[0:5]

animals_category

plt.pie(animals_category.protected, autopct="%0.1f%%")
plt.axis=('equal')
plt.legend(animals_category.category)
plt.show()

#make same table except only including animals
new_category_pivot_sorted = category_pivot_sorted[0:5]
#bar graph 
plt.close('all')
plt.figure(figsize=(12,8))
animals = new_category_pivot_sorted.category.values
plt.bar(range(len(animals)),new_category_pivot_sorted.not_protected)
plt.bar(range(len(animals)),new_category_pivot_sorted.protected, bottom = new_category_pivot_sorted.not_protected)
ax1 = plt.subplot()
ax1.set_xticks(range(len(animals)))
ax1.set_xticklabels((animals))
plt.ylabel('Number of Species')
plt.title('Protection by Category')

legend_labels = ['Not Protected','Protected']
plt.legend(legend_labels)


plt.show()
                      

from scipy.stats import chi2_contingency


contingency = [[146,30],[413,75],[72,7],[115,11],[73,5]]
chi2_test = chi2,pval,dof,expected = chi2_contingency(contingency)
chi2_test


contingency_bird_fish= [[413,75],[115,11]]
test_1= _,pval_bird_fish,_,_ = chi2_contingency(contingency_bird_fish)
pval_bird_fish
test_1


contingency_mam_bird = [[146,30],[413,75]]
test_2 = _, pval_mam_bird, _,_ = chi2_contingency(contingency_mam_bird)
if pval_mam_bird<.05:
    print "With a pval of %s we can reject the null, meaning there is a relationship in the difference that could mean they're related." % (pval_mam_bird)
else:
    print 'With a pval of %s we can assume these variables are independant of each other.' % (pval_mam_bird)
    
test_2



contingency_rep_mam= [[73,5],[146,30]]
_,pval_rep_mam,_,_ = chi2_contingency(contingency_rep_mam)
if pval_rep_mam<0.05:
    print "With a pval of %s we can reject the null hypothesis, meaning there could be a relationship between the variables." % (pval_rep_mam)
else:
    print 'With a pval of %s we can assume these variables are independant of each other.' % (pval_rep_mam)


observations = pd.read_csv('observations-Copy1.csv')
observations.head(10)


species1['is_sheep']= species1.common_names.apply(lambda x: 'Sheep' in x)
species1.head()

sheep_species = species1[(species1.is_sheep) & (species1.category == 'Mammal')]
sheep_species.head()

sheep_observations = pd.merge(sheep_species, observations)

sheep_observations1 = sheep_observations.groupby(['scientific_name','park_name','is_protected']).observations.sum().reset_index().sort_values(by='park_name')

sheep_observations1_pivot = sheep_observations1.pivot(index = 'scientific_name',columns =                                                       'park_name', values = 'observations').reset_index()
sheep_observations1_pivot.columns = ['scientific_names','Bryce',"Great Smoky Mountains", 'Yellowstone', 'Yosemite' ]
sheep_observations1_pivot


obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()
obs_by_park


plt.figure(figsize=(16,4))
ax = plt.subplot()
plt.bar(range(len(obs_by_park.park_name)), obs_by_park.observations)
ax.set_xticks(range(len(obs_by_park.park_name)))
ax.set_xticklabels(obs_by_park.park_name.values)
ax.set_ylabel('Number of Observations')
plt.title('Observations of Sheep per Week')
plt.show()


minimum_detectable_effect = 100* .05/.15
minimum_detectable_effect 


sample_size = 510

bryce = float(510/250)
yellowstone = float(510/507)


print '%s week is needed to observe 510 samples of sheepat Yellowstone. %s weeks are needed to observe 510 sheep at Bryce National Park. ' % (yellowstone,bryce)

