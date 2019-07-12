# Within R
library(MBatch)
# Set these environment variable to override file locations if needed
#
Sys.setenv(MBATCH_TEST_OUTPUT="/Users/ak29/Downloads/output")
Sys.setenv(MBATCH_TEST_INPUT="/Users/ak29/Downloads/MATRIX_DATA")
Sys.setenv(MBATCH_TEST_COMPARE="/Users/ak29/Downloads/COMPARE")
baseDir <- file.path("/Users/ak29/Downloads/MBatch-master/package/tests")
message(baseDir)
testFiles <- list.files(path=baseDir)
print(testFiles)
results <- c()
for(myFile in testFiles)
{
  message("************************************************************")
  message("************************************************************")
  message("**** ", file.path(baseDir, myFile))
  message("************************************************************")
  message("************************************************************")
  test <- source(file.path(baseDir, myFile))
  if (isTRUE(test$value))
  {
    results <- c(results, paste("Test succeeded for ", myFile, sep=""))
  }
  else
  {
    results <- c(results, paste("Test failed for ", myFile, sep=""))
  }
}
print(results)

