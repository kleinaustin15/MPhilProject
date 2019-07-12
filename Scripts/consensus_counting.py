#import necessary packages
import os
import pandas as pd 

#create antibody to gene dictionary
df3 = pd.read_csv('Antibodies_to_Genes.csv')
antibody_gene_dict = {}
for index, row in df3.iterrows():
	antibody_gene_dict[row['Antibodies']] = row['Genes']

#run through all drugs and all drug action pathways
while True:
	pathway = input('Enter pathway: ')
	os.chdir('/Users/ak29/Desktop/Single Agent Files/'+pathway+' drugs')
	drugs = []
	consensus_count = []
	RPPA_only_count = []
	voom_only_count = []
	for roots, dirs, files in os.walk('.'):
		for drug in dirs:
			drugs.append(drug)
			os.chdir('/Users/ak29/Desktop/Single Agent Files/'+pathway+' drugs/'+drug)
			cwd = os.getcwd()
			RPPA_name_list = []
			voom_name_list = []
			for root,dirs,files in os.walk('.'):
				#read in RPPA and RNA-seq significant protein/gene lists
				for name in files:
					if name[-21:-12] == '_voom_sig':
						df1 = pd.read_csv(name)
						for index1, row1 in df1.iterrows():
							voom_name_list.append(row1['name'])
					elif name[-21:-12] == '_RPPA_sig':
						df2 = pd.read_csv(name)
						for index2, row2 in df2.iterrows():
							try:
								RPPA_name_list.append(antibody_gene_dict[row2['name']])
							except KeyError:
								RPPA_name_list.append(row2['name'])
			#find consensus, RPPA_only, and RNA-seq only sets
			consensus = set(RPPA_name_list) & set(voom_name_list)
			RPPA_only = [name for name in RPPA_name_list if name not in consensus]
			voom_only = [name for name in voom_name_list if name not in consensus]
			consensus_count.append(len(consensus))
			RPPA_only_count.append(len(RPPA_only))
			voom_only_count.append(len(voom_only))
	count_df = pd.DataFrame({'Drug':drugs, 'Common':consensus_count, 'RPPA_only':RPPA_only_count, 'voom_only':voom_only_count})
	os.chdir('/Users/ak29/Desktop/Single Agent Files/'+pathway+' drugs')
	count_df.to_csv(pathway+'_RPPA_and_voom_consensus_count.csv')
			
					
