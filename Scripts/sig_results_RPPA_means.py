#import packages
import os
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

all_means = []

pathway = input('Enter pathway: ')

#run through all drugs in all drug action pathways
while pathway != 'complete':
	os.chdir('/Users/ak29/Desktop/Single Agent Files/'+pathway+' drugs')
	for roots, dirs, files in os.walk('.'):
		for drug in dirs:
			os.chdir('/Users/ak29/Desktop/Single Agent Files/'+pathway+' drugs/'+drug)
			cwd = os.getcwd()
			for root,dirs,files in os.walk('.'):
				for name in files:
					if name[-40:-15] == 'RPPA_and_voom_results_100':
						df =pd.read_csv(name)
						mean_list = df['mean'].tolist()
						for value in mean_list:
							all_means.append(value)
	pathway = input('Enter pathway: ')

#calculate mean and standard deviation for the distribution of weights
total_mean = np.mean(all_means)
total_std = np.std(all_means)
pos_sig_range = total_mean+2*(total_std)
neg_sig_range = total_mean-2*(total_std)
print(pos_sig_range)
print(neg_sig_range)
plt.boxplot(all_means,vert=False)
plt.title('Distribution of Weights ' + 'mean: ' + str(total_mean) + ' std: ' + str(total_std))
plt.axvline(x=pos_sig_range)
plt.axvline(x=neg_sig_range)
plt.show()

'''0.22687810605049466
-0.205328200006508'''

'''0.1219468110732862
-0.11244819527927358'''

'''0.11997256428
-0.113521964368'''


