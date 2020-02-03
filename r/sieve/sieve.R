sieve <- function(limit) {
    if (limit < 2)
        return(NULL)
    candidates <- 2:limit
    primes <- NULL
    while (length(candidates) > 0) {
        candidate <- candidates[1]
        primes <- c(primes, candidate)
        candidates <- candidates[candidates %% candidate != 0]
    }
    return(primes)
}
