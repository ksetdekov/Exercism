hamming <- function(strand1, strand2) {
    tovector <- function(strand) {
        unlist(strsplit(strand, NULL))
    }
    strand1vector <- tovector(strand1)
    strand2vector <- tovector(strand2)
    
    if (length(strand1vector) != length(strand2vector))
        stop('input not positive')
    sum(strand1vector != strand2vector)
}