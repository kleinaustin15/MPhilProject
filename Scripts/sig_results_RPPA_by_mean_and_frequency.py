#import necessary packages
import os
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

#continuous loop for running through all drugs and all drug pathways
while True:
	pathway = input('Enter pathway: ')
	os.chdir('/Users/ak29/Desktop/Single Agent Files/'+pathway+' drugs')
	for roots, dirs, files in os.walk('.'):
		for drug in dirs:
			os.chdir('/Users/ak29/Desktop/Single Agent Files/'+pathway+' drugs/'+drug)
			cwd = os.getcwd()
			for root,dirs,files in os.walk('.'):
				for name in files:
					if name[-40:-15] == 'RPPA_and_voom_results_100':
						sig_dataframe = pd.DataFrame()
						sig_name_list = []
						sig_mean_list = []
						sig_freq_list = []
						df =pd.read_csv(name)
						for index, row in df.iterrows():
							#filter out any significant proteins that fall within +- 2std
							if row['mean'] > 0.11997256428 or row['mean'] < -0.113521964368: 
								#filter out any significant proteins with a frequency lower than 0.8
								if row['frequency'] > 0.8:
									sig_name_list.append(row['name'])
									sig_mean_list.append(row['mean'])
									sig_freq_list.append(row['frequency'])
						sig_dataframe['name'] = sig_name_list
						sig_dataframe['mean'] = sig_mean_list
						sig_dataframe['freq'] = sig_freq_list
						sig_dataframe.to_csv(drug+'_RPPA_and_voom_sig_results.csv')




						