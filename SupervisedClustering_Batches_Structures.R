library(MBatch)
# set the paths
theGeneFile <- "/Users/ak29/Desktop/Single\ Agent\ Files/RPPA/ANY_Corrections_Separate_Batches-RBN_Replicates.txt" 
theBatchFile <- "/Users/ak29/Desktop/Single\ Agent\ Files/RPPA/batch_info_RBN_Separate_Batches.txt" 
theOutputDir <- "/Users/ak29/Desktop/Single\ Agent\ Files/RPPA/MBatch_results/SupervisedClustering_RBN_Separate_Batches"
# make sure the output dir exists and is empty
unlink(theOutputDir, recursive=TRUE)
dir.create(theOutputDir, showWarnings=FALSE, recursive=TRUE)
# load the data and reduce the amount of data to reduce run time
myData <- mbatchLoadFiles(theGeneFile, theBatchFile)
# here, we take most defaults
SupervisedClustering_Batches_Structures(theData=myData,
                                        theTitle="All Batches Supervised Clustering",
                                        theOutputPath=theOutputDir,
                                        theDoHeatmapFlag=TRUE)