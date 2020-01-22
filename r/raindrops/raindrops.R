raindrops <- function(number) {
    dplyr::case_when(
        number %% 105 == 0 ~ "PlingPlangPlong",
        number %% 15 == 0 ~ "PlingPlang",
        number %% 21 == 0 ~ "PlingPlong",
        number %% 35 == 0 ~ "PlangPlong",
        number %% 3 == 0 ~ "Pling",
        number %% 5 == 0 ~ "Plang",
        number %% 7 == 0 ~ "Plong",
        TRUE ~ as.character(number)
    )
}