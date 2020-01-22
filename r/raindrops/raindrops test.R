raindrops <- function(number) {
    if (number %% 3 == 0) {
        result <- "Pling"
    }
    if (number %% 5 == 0) {
        result <- paste0(result, "Plang")
    }
    if (number %% 7 == 0) {
        result <- paste0(result, "Plong")
    }
    if (!exists("result")) {
        result <- as.character(number)
    }
    result
}