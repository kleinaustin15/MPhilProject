#import package
import csv

#read in IC50 file and drug action pathway names
effector_pathway = input('Enter effector pathway: ')
main_file = open('GDSC_owned_fitted_rapid_screen_v1.2.0_20181002.csv','r')
data = csv.reader(main_file,skipinitialspace=True)
drug_file = open(effector_pathway+'_subset_fitted_rapid_screen_v1.2.0_20181002.csv', 'w')
drug_file_writer = csv.writer(drug_file,delimiter=',')

#sort through IC50 values for only those matching drug action pathway
for line in data:
	if line[1] == 'DRUG_ID':
		drug_file_writer.writerow(line)
	elif line[5] == effector_pathway:
		drug_file_writer.writerow(line)
main_file.close()
drug_file.close()