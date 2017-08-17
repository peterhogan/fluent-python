from matplotlib import use as matuse
matuse('Agg')

import random_dist as rd
import matplotlib.pyplot as plt
import numpy as np

rand = rd.Random(1,1,10**6)
samp_ar = np.array(rand.getsample(100))
train_ar = np.array(rand.getsample(250))
all_ar = np.array(rand.values)
plt.hist(samp_ar,alpha=0.5, label='sample', normed=True)
plt.hist(train_ar,alpha=0.5, label='train', normed=True)
plt.hist(all_ar,alpha=0.5, label='all', normed=True)
plt.legend(loc='upper right')
plt.savefig('./plot.png')
print('Done!')
