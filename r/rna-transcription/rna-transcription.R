to_rna <- function(dna) {
    converter <- function(amino) {
        if (!(amino %in% c("C", "G", "T", "A")))
            stop('unallowed input characters')
        c("G", "C", "A", "U")[match(amino, c("C", "G", "T", "A"))]
    }
    paste0(unlist(lapply(unlist(
        strsplit(dna, NULL)
    ), converter)), collapse = '')
}