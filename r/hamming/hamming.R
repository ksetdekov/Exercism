hamming <- function(strand1, strand2) {
    if (nchar(strand1) != nchar(strand2))
        stop('input not positive')
    tovector <- function(strand) {
        unlist(strsplit(strand, NULL))
    }
    strand1vector <- tovector(strand1)
    strand2vector <- tovector(strand2)
    sum(strand1vector != strand2vector)
}