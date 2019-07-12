library(MBatch)
# set the paths
invariantFile="/Users/ak29/Desktop/Single\ Agent\ Files/RPPA/CCLE_COSMIC_invariant.txt"
variantFile="/Users/ak29/Desktop/Single\ Agent\ Files/RPPA/MCLP_COSMIC_variant.txt"
theOutputDir="/Users/ak29/Desktop/Single\ Agent\ Files/RPPA/MBatch_results/RBN_CCLE_MCLP"
theRandomSeed=314
resolveDuplicates <- function(theNames)
{
  # keep first instance of a name
  # number subsequent ones starting with .1
  make.unique(theNames)
}
readRPPAdataAsMatrix_WithTab <- function(theFile)
{
  # read RPPA data as a dataframe
  # column rppaDF[,1] contains row names that may contain duplicates
  rppaDF <- readAsGenericDataframe(theFile)
  # resolve duplicates in row names here
  myRownames <- rppaDF[,1]
  myRownames <- resolveDuplicates(myRownames)
  # convert to matrix
  myMatrix <- data.matrix(rppaDF[,-1])
  rownames(myMatrix) <- myRownames
  t(myMatrix)
}
readRPPAdataAsMatrix_NoInitialTab <- function(theFile)
{
  # read RPPA data as a dataframe
  # column rppaDF[,1] contains row names that may contain duplicates
  rppaDF <- read.table(theFile, header=TRUE, sep="\t", as.is=TRUE,
                       check.names=FALSE, stringsAsFactors=FALSE,
                       colClasses="character", na.strings="NA",
                       row.names=NULL)
  # resolve duplicates in row names here
  myRownames <- rppaDF[,1]
  myRownames <- resolveDuplicates(myRownames)
  # convert to matrix
  myMatrix <- data.matrix(rppaDF[,-1])
  rownames(myMatrix) <- myRownames
  t(myMatrix)
}
# make sure the output dir exists and is empty
unlink(theOutputDir, recursive=TRUE)
dir.create(theOutputDir, showWarnings=FALSE, recursive=TRUE)
message("Reading invariant file")
invMatrix = readRPPAdataAsMatrix_WithTab(invariantFile)
message("Reading variant file")
varMatrix = readRPPAdataAsMatrix_WithTab(variantFile)
filename <- RBN_Replicates(theInvariantMatrix=invMatrix,
                           theVariantMatrix=varMatrix,
                           theInvariantGroupId="CCLE",
                           theVariantGroupId="MCLP",
                           theMatchedReplicatesFlag=TRUE,
                           theCombineOnlyFlag=FALSE,
                           thePath=theOutputDir,
                           theWriteToFile=TRUE)