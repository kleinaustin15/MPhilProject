#import packages
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

#read through RPPA file calculating Pearson correlation for every cell line pair within a batch/dataset
all_data = []
for i in range(5):
	filename = input('Enter filename:')
	df = pd.read_csv(filename+'.csv')
	corr_mat = df.corr(method='pearson')
	upper_tri = corr_mat.where(np.triu(np.ones(corr_mat.shape)).astype(np.bool))
	upper_tri = upper_tri.stack().reset_index()
	upper_tri.columns = ['Row','Column','Value']
	data = upper_tri.loc[:,'Value'].tolist()
	all_data.append(data)

#calculate Pearson correlation only for repeated cell lines
filename = input('Enter filename:')
df = pd.read_csv(filename+'.csv')
corr_mat = df.corr(method='pearson')
upper_tri = corr_mat.where(np.triu(np.ones(corr_mat.shape)).astype(np.bool))
upper_tri = upper_tri.stack().reset_index()
upper_tri.columns = ['Row','Column','Value']
data = []
for index, row in upper_tri.iterrows():
    if row['Row']+'.1' == row['Column'] or row['Row']+'.2' == row['Column'] :
        data.append(row['Value'])
all_data.append(data)

#plot Pearson correlation distributions for each dataset/grouping
plt.boxplot(all_data,vert=False)
plt.title('RBN Correlation Boxplot')
plt.yticks([1,2,3,4,5,6],['ALL','GDSC_A','GDSC_B','MCLP','CCLE','Repeated'])
plt.show()


