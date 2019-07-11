# import necessary packages
import pandas as pd
import numpy as np
import math
from scipy.stats import norm, shapiro,kstest,normaltest
import matplotlib.pyplot as plt  

#read in protein distribution data files
df1 = pd.read_csv('CCLE_only_COSMIC.csv')
df2 = pd.read_csv('MDA_only_COSMIC.csv')

#create antibody lists from data files
antibodies1 = list(df1.columns.values)
antibodies2 = list(df2.columns.values)
antibodies1.pop(0) 
antibodies2.pop(0)

#create empty pandas dataframe
regressions = pd.DataFrame(index=range(0,1),columns=['mu','std','Shapiro','p-value','KS','p-value','D\'Agostino','p-value'],dtype=float)

#calculate normality tests for each antibody
for protein in antibodies2:
	data = df2.loc[:,protein].tolist()
	'''data[:] = [x for x in data if math.isnan(x) == False]'''
	mu,std = norm.fit(data)
	sh = shapiro(data)
	ks = kstest(data,'norm',args=(mu,std))
	da = normaltest(data)
	regressions.loc[protein] = [mu,std,sh[0],sh[1],ks[0],ks[1],da[0],da[1]]
	
regressions.to_csv('expression_normal_distributions_shapiro_MDA.csv')