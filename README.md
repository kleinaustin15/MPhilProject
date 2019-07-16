# MPhilproject

Characterisation of a Proteomic Dataset for Biomarker Discovery in Cancer Cell Lines

Antibody Distributions - Contains png files with distribution graphs for every antibody in the CCLE dataset. Each graph also 
has a normal regression plotted with the mean and standard deviation of that normal regression in the title of each graph.

Antibody Heatmaps - Contains png files with heatmaps for antibodies and their phosphoryalted forms in order to compare
distributions of each protein across cell lines

Datasets - Contains all necessary datasets to recereate and generate all results from the dissertation
        
        DepMap-2019q1-celllines_v2.csv - Updated cell line list for conversion from COSMIC ID's to any other cell line           
            labeling
        
        GDSC_owned_fitted_rapid_screen_v1.2.0_20181002.csv.zip - csv file containing IC50 values for 280 drugs covering more 
            than 800 cell lines
        
        NO_RBN_ALL_Batches.csv - csv file containing consensus dataset prior to RBN
        
        RBN_RPPA_ALL_Batches_Repeates_Averaged.csv - csv file containing consensus dataset after RBN
        
        model_list_latest.csv - Cell list which covers some missing cell lines from DepMap file
        
        spearman_correlation_antibody_to_gene.csv - csv file containing spearman correlation values for genes and proteins
            within the RPPA and RNA-seq datasets
  
Scripts - Contains all scripts necessary to recreate all results from the dissertation
       
       MBatch_test.R - R file for testing the correct installation of MBatch and all packages required to run MBatch
       
       PCA_Regular_Structure.R - R file for creating prinicpal component analysis (PCA) plots 
       
       RBN.R - R file for running replicates based normalisation (RBN) to remove batch effects from datasets
       
       SupervisedClustering_Batches_Structures.R - R file for creating heatmaps from RPPA datasets
       
       consensus_counting.py - python file used to compare RPPA and RNA-seq elastic net results on a drug by drug basis
       
       effector_pathway.py - python file used to split drugs in GDSC_owned_fitted_rapid_screen_v1.2.0_20181002.csv.zip 
            by drug action pathway
       
       elastic_net_RPPA.py - python file used to run the elastic net regression of the RPPA and ENA-seq datasets
       
       expression_distribution.py - python file for drawing distribution graphs for each antibody in a given RPPA dataset
       
       lin_reg.py - python file used to generate linear regression graphs for repeated cell lines across the datasets
       
       pearson_correlation.py - python file used to calculate pearson correlation values for cell lines within the RPPA 
            datasets
       
       sig_heatmap.R - R file for creating heatmaps for significant drugs 
       
       sig_results_RPPA_by_mean_and_frequency.py - python file for filtering elastic net results by mean weight and 
            frequency for each significant protein
       
       sig_results_RPPA_means.py - python file for calculating the mean cut-offs for running      
            sig_results_RPPA_by_mean_and_frequency.py, can also calculate frequency cut-off if necessary
       
       spearman_correlation.py - python file for calculating spearman correlation values for gene-protein pairs

Significant Protein Heatmaps - Contains png files with heatmaps of significant proteins from RPPA elastic net for each drug 
        action pathway 

