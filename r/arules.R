library(arules)
library(arulesViz)

setwd("~/TTU-SOURCES/harvey-classifier/r")

tr <- read.transactions("data/transactions.csv", format = "basket", sep=",", skip = 1)

frequentItems <- eclat (tr, parameter = list(supp = 0.05, maxlen = 50)) # calculates support for frequent items
inspect(frequentItems)
#>    items                         support   
#> 1  {other vegetables,whole milk} 0.07483477
#> 2  {whole milk}                  0.25551601
#> 3  {other vegetables}            0.19349263
#> 4  {rolls/buns}                  0.18393493
#> 5  {yogurt}                      0.13950178
#> 6  {soda}                        0.17437722
itemFrequencyPlot(tr, topN=15, type="absolute", main="Item Frequency") # plot frequent items


rules <- apriori (tr, parameter = list(supp = 0.02, conf = 0.5)) # Min Support as 0.001, confidence as 0.8.
rules_conf <- sort (rules, by="confidence", decreasing=TRUE) # 'high-confidence' rules.
inspect(head(rules_conf)) # show the support, lift and confidence for all rules

plot(rules)