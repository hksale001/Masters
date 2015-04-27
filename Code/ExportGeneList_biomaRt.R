#Set Library and dataset
library("biomaRt")
ensembl=useMart("ensembl")
ensembl = useDataset("hsapiens_gene_ensembl",mart=ensembl)

#To see list if available filters and attributes
filters = listFilters(ensembl)
filters[1:5,]
attributes = listAttributes(ensembl)
attributes[1:5,]

#To get desired ouput
columns = c('ensembl_gene_id','chromosome_name','start_position','end_position','strand','band','external_gene_name','description','goslim_goa_accession')
qfilters=c('chromosome_name', 'start','end')
values=list(6, 28500000, 33490000)
getBM(columns, qfilters, values, mart=ensembl) -> dat1

#Structure of output
is.data.frame(dat1)
str(dat1)
head(dat1)

#Export to file
write.table(dat1,file = "MHCGeneList_biomaRt.txt",quote=FALSE, sep="\t", na="", row.names=FALSE)
