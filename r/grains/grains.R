square <- function(n) {
    if (n < 1 | n > 64)
        stop('Square out of bounds')
    2^(n-1)
}

total <- function() {
    sum(sapply(1:64, square))
}
