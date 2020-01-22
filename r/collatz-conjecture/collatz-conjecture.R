collatz_step_counter <- function(num) {
    result <- NULL
    stepcounter <- function(n) {
        if (n <= 0)
            stop('input not positive')
        if (n == 1)
            0
        else if (n %% 2 == 0)
            1 + stepcounter(n / 2)
        else
            1 + stepcounter(3 * n + 1)
    }
    sapply(num, stepcounter)
}
