parse_phone_number <- function(number_string) {
    if (nchar(number_string) < 10)
        return(NULL)
    numvector <- as.numeric(strsplit(number_string, NULL)[[1]])
    numvector <- numvector[!is.na(numvector)]
    if (length(numvector) < 10 | length(numvector) > 11)
        return(NULL)
    if (length(numvector) == 10) {
        cleared <- numvector
    } else {
        if (numvector[1] == 1) {
            cleared <- numvector[2:11]
        } else {
            return(NULL)
        }
    }
    result <- paste0(cleared, collapse = "")
    if (regexpr("[2-9][0-9]{2}[2-9][0-9]{6}", result)[[1]] < 0) {
        return(NULL)
    }
    result
}