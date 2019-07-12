#import necessary packages
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

#read in protein and gene expression files
df1 = pd.read_csv('RPPA_and_voom_for_correlation.csv')
df2 = pd.read_csv('Antibodies_to_Genes.csv')

#dictionary connecting proteins to genes
antibody_gene_dict = {}
for index, row in df2.iterrows():
	antibody_gene_dict[row['Antibodies']] = row['Genes']

#calculate spearman correlation values for each protein to gene pair
corr_mat = df1.corr(method='spearman')
upper_tri = corr_mat.where(np.triu(np.ones(corr_mat.shape)).astype(np.bool))
upper_tri = upper_tri.stack().reset_index()
upper_tri.columns = ['Row','Column','Value']
data = []
columns = []
rows = []
for index, row in upper_tri.iterrows():
    try:
    	if antibody_gene_dict[row['Row']] == row['Column']:
        	data.append(row['Value'])
        	columns.append(row['Column'])
        	rows.append(row['Row'])
    except KeyError:
    	print(row['Row'],row['Column'])
final_dict = {'Row':rows, 'Column':columns, 'Value':data}
df3 = pd.DataFrame(final_dict)
df3.to_csv('spearman_correlation_antibody_to_gene.csv')

