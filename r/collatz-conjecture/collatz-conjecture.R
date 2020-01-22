collatz_step_counter <- function(num) {
    result <- NULL
    stepcounter <- function(victim) {
        n <- 0
        while (victim > 1) {
            victim <- ifelse(victim %% 2 == 0, victim / 2, victim * 3 + 1)
            n <- n + 1
        }
        n
    }
    if (num <= 0)
        stop('input not positive')
    for (num1 in num) {
        resulti <- stepcounter(num1)
        result[length(result) + 1] <- resulti
    }
    result
}
