import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Upload homework2_data.csv file as: df = pd.read_csv(`homework2_data.csv`)
df = pd.read_csv('homework2_data.csv')

# This csv file has columns ['delta_frame_time', 'dns_answers_ttl',
# 'is_cc_provider', 'is_ip_private', 'delay']
col1 = df['delta_frame_time'].values
col2 = df['dns_answers_ttl'].values
col3 = df['is_cc_provider'].values
col4 = df['is_ip_private'].values
col5 = df['delay'].values

# You can extract each column as an array: col = df['name_of_col'].values
# Take a look at data in each column.
# What type of data each column contains (ordinal, nominal, discerete or continuous)?
print(f'delta_frame_time = {df['delta_frame_time'].values}')   # discrete
print(f'dns_answers_ttl = {df['dns_answers_ttl'].values}')    # discrete
print(f'is_cc_provider = {df['is_cc_provider'].values}')  # discrete
print(f'is_ip_private = {df['is_ip_private'].values}')    # discrete
print(f'delay = {df['delay'].values}')     # continuous

# Use plt.hist() to plot a histogram for each feature.
#plt.subplots(1,3, figsize=(9, 3),sharey=True)
# What is the distribution of each feature?
# Use np.mean() and np.median() to find mean and median values of each feature.
# Use plt.axvline() to plot mean and median of each feature.
plt.figure(figsize=(12, 7))
plt.subplot(231)
plt.title(label='delta_frame_time')
plt.hist(col1, color='green', edgecolor="white")    # not Normal
plt.axvline(x=np.median(col1), color='red')
plt.axvline(x=np.mean(col1), color='orange')

plt.subplot(232)
plt.title(label='dns_answers_ttl')
plt.hist(col2, edgecolor="white")    # not Normal
plt.axvline(x=np.median(col2), color='red')
plt.axvline(x=np.mean(col2), color='orange')

plt.subplot(233)
plt.title(label='is_cc_provider')
plt.hist(col3, color='green')     # not Normal
plt.axvline(x=np.median(col3), color='red')
plt.axvline(x=np.mean(col3), color='orange')

plt.subplot(234)
plt.title(label='is_ip_private')
plt.hist(col4, color='gray')    # not Normal
plt.axvline(x=np.median(col4), color='red')
plt.axvline(x=np.mean(col4), color='orange')

plt.subplot(235)
plt.title(label='delay')
plt.hist(col5, 30, edgecolor="white")    # close to Normal
plt.axvline(x=np.median(col5), color='red')
plt.axvline(x=np.mean(col5), color='orange')
plt.show()

