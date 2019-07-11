library(MBatch)
#used for PCA plotting
isTrendBatch<-function(theBatchTypeName, theListOfBatchIds)
{
  return(is.element(theBatchTypeName, c("ShipDate")))
}
# set the paths
theGeneFile <- "/Users/ak29/Desktop/Single\ Agent\ Files/RPPA/ANY_Corrections_Separate_Batches-RBN_Replicates.txt" 
theBatchFile <- "/Users/ak29/Desktop/Single\ Agent\ Files/RPPA/batch_info_RBN_Separate_Batches.txt" 
theOutputDir <- "/Users/ak29/Desktop/Single\ Agent\ Files/RPPA/MBatch_results/PCA_RBN_Separate_Batches"
# make sure the output dir exists and is empty
unlink(theOutputDir, recursive=TRUE)
dir.create(theOutputDir, showWarnings=FALSE, recursive=TRUE)
# load the data and reduce the amount of data to reduce run time
myData <- mbatchLoadFiles(theGeneFile, theBatchFile)
# here, we take most defaults
PCA_Regular_Structures(theData=myData,
                       theTitle="ALL_batches_no_missing_data_PCA",
                       theOutputPath=theOutputDir,
                       theBatchTypeAndValuePairsToRemove=NULL,
                       theBatchTypeAndValuePairsToKeep=NULL,
                       theDoDscPermsFileFlag = TRUE,
                       theIsPcaTrendFunction=isTrendBatch,
                       theDSCPermutations=1000,
                       theDSCThreads=1,
                       theMinBatchSize=2,
                       theJavaParameters="-Xms2000m",
                       theSeed=theRandomSeed,
                       theMaxGeneCount=10000)