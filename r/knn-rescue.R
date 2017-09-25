# Set seed for reproducible results
set.seed(100)

# Packages
library(tm) # Text mining: Corpus and Document Term Matrix
library(class) # KNN model
library(SnowballC) # Stemming words
library(ROCR)
library(stringr)


setwd("~/TTU-SOURCE/harvey-classifier/r")

# Read csv with two columns: text and category
df <- read.csv("data/labeled-rescue-1000.csv", sep =",", header = TRUE)
df$text = str_replace_all(df$text,"[^[:graph:]]", " ") 

# Create corpus
docs <- Corpus(VectorSource(df$text))

# Clean corpus
docs <- tm_map(docs, content_transformer(tolower))
docs <- tm_map(docs, removeNumbers)
docs <- tm_map(docs, removeWords, stopwords("english"))
docs <- tm_map(docs, removePunctuation)
docs <- tm_map(docs, stripWhitespace)
docs <- tm_map(docs, stemDocument, language = "english")

# Create dtm
dtm <- DocumentTermMatrix(docs)

# Transform dtm to matrix to data frame - df is easier to work with
mat.df <- as.data.frame(data.matrix(dtm), stringsAsfactors = FALSE)

nrow(mat.df)
ncol(mat.df)

# Column bind category (known classification)
mat.df <- cbind(mat.df, df$label)

# Change name of new column to "category"
colnames(mat.df)[ncol(mat.df)] <- "labeled-rescue"
ncol(mat.df)

# Split data by rownumber into two equal portions
train <- sample(nrow(mat.df), ceiling(nrow(mat.df) * .50))
test <- (1:nrow(mat.df))[- train]

length(train)
length(test)

# Isolate classifier
cl <- mat.df[, "labeled-rescue"]

# Create model data and remove "category"
modeldata <- mat.df[,!colnames(mat.df) %in% "labeled-rescue"]

# Create model: training set, test set, training set classifier
knn.pred <- knn(modeldata[train, ], modeldata[test, ], cl[train], prob = TRUE, k = 2)

# Confusion matrix
conf.mat <- table("Predictions" = knn.pred, Actual = cl[test])
conf.mat

# Accuracy
(accuracy <- sum(diag(conf.mat))/length(test) * 100)

# Create data frame with test data and predicted category
# df.pred <- cbind(knn.pred, modeldata[test, ])
# write.table(df.pred, file="output.csv", sep=";")


prob <- attr(knn.pred , "prob")
pred_knn <- performance(knn.pred, "tpr", "fpr")
plot(pred_knn, avg= "threshold", colorize=T, lwd=3, main="a ROC curve!")

## sample ROCR curve
data(ROCR.simple)
pred <- prediction( ROCR.simple$predictions, ROCR.simple$labels )
pred2 <- prediction(abs(ROCR.simple$predictions + 
                          rnorm(length(ROCR.simple$predictions), 0, 0.1)), 
                    ROCR.simple$labels)
perf <- performance( pred, "tpr", "fpr" )
perf2 <- performance(pred2, "tpr", "fpr")
plot( perf, colorize = TRUE)
plot(perf2, add = TRUE, colorize = TRUE)


