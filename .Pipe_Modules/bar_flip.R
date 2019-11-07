#!/usr/bin/env Rscript

library("getopt")

#Read in flags
spec <- matrix(c(
  'input_bar',   'i', 1, "character",
  'output_bar',  'o', 1, "character",
  'nThreads',    'n', 1, "integer",
  'config_text', 'f', 1, "character"),
byrow=TRUE, ncol=4)
    
opt <- getopt(spec)
    
#read the file and flip it
bar <- readLines(con=opt$input_bar)
bar <- paste(rev(strsplit(bar, NULL)[[1]]), collapse='')

#append what was supplied at the config
bar <- paste(bar,opt$config_text, sep=' ')

#Write it out
writeLines(bar, con=opt$output_bar)
