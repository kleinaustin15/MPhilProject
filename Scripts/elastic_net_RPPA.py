import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from gdsctools import gdsctools_data, regression, GenomicFeatures, IC50
#A function to run ElasticNet regression on a given drug IC50 matrix file
#with an RPPA file.
#
#drug_name: a str corresponding to drug name
#file_name: a str corresponding to the IC50 matrix file name 
#
#Returns: a csv file containing the results of ElasticNet regression
def merged_voom_analysis(drug_name,file_name,replicate):
	gf = GenomicFeatures('RPPA_and_voom_combined.csv')
	gd = regression.GDSCElasticNet(file_name,gf)
	#check that program is running correctly
	print(gd)
	matrix_file = open(file_name,'r')
	matrix_file_list = matrix_file.readlines()
	line_1 = matrix_file_list[0].split(',')
	drugid = int(line_1[1].strip())
	matrix_file.close()
	#runCV may take several hours if many genomic features are involved
	res = gd.runCV(drugid,kfolds=10)
	alpha=res.alpha
	best_model = gd.get_model(alpha=alpha)
	res = gd.plot_weight(drugid,best_model)
	#creates new file and stores results of ElasticNet regression
	res.to_csv(drug+'_RPPA_and_voom_results_holder.csv')
	df = pd.read_csv(drug+'_RPPA_and_voom_results_holder.csv')
	plt.close("all")
	return df


#Walk through folders to run EN on each drug
while True:
	pathway = input('Enter pathway: ')
	os.chdir('/Users/ak29/Desktop/Single Agent Files/'+pathway+' drugs')
	for roots, dirs, files in os.walk('.'):
		for drug in dirs:
			os.chdir('/Users/ak29/Desktop/Single Agent Files/'+pathway+' drugs/'+drug)
			cwd = os.getcwd()
			for root,dirs,files in os.walk('.'):
				for name in files:
					if name[-5] == 'x':
						for i in range(100):
							result = merged_voom_analysis(drug,name,str(i))
							if i == 0:
								final = result
							else:
								final = final.merge(result,on = 'name',how = 'outer')
						all_values = final.values.tolist()
						means = []
						frequencies = []
						for item in all_values:
							try:
								means.append(np.nanmean(item[1:]))
								cleaned = [value for value in item if str(value) != 'nan']
								frequencies.append(len(cleaned[1:])/100)
							except TypeError:
								means.append(0)
								frequencies.append(0)	
						final['mean'] = means
						final['frequency'] = frequencies
						final.to_csv(drug+'_RPPA_and_voom_results_100_replicates.csv')
