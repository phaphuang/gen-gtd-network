#---
#  title: "genGraph_China"
#author: "Kanokwan"
#date: "10/24/2018"
#output: html_document
#---
#```{r}
#China
#install.packages("igraph")
library(igraph)

gtd = read.csv("gtd_China.csv", header = T, sep=",")

#select only the column we need to perform graph
gtdChina  = gtd[ ,c("gname", "tname")]

#transform data to be adjacency matrix
myAdMatrix = get.adjacency(graph.edgelist(as.matrix(gtdChina), directed=T))

#transform adjacency matrix to the graph object
gtdGraphChina = graph.adjacency(myAdMatrix, mode = "undirected")


#plot the graph
plot(gtdGraphChina)
#```
