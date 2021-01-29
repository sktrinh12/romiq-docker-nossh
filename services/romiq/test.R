args <- commandArgs(trailingOnly=TRUE)
rerun_rd <- FALSE

# test if there is one argument
if (length(args) == 0) {
    stop("At least one argument must be supplied (barcode).n", call.=FALSE)
} else if (length(args) == 2) {
    if (as.logical(toupper(args[2])) == TRUE) {
        rerun_rd <- TRUE
    }
}

print(R.Version())
print(paste(rep("+",25), collapse=''))
print(paste0("the arguments: ", args))
print(paste0('re-run: ', rerun_rd))

for (i in seq(1:3)) {
    Sys.sleep(1)
    print(paste0(i, '...'))
}
