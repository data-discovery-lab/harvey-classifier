library(ROCR)

# Generate fake data
isolet_training <- sweep(matrix(rnorm(400), 40, 10), 1, rep(0:1, each=20))
isolet_testing <- sweep(matrix(rnorm(400), 40, 10), 1, rep(0:1, each=20))
# Generate class labels
cl <- cl_testing <- rep(c(-1, 1), each=20)

knn_isolet <- knn(isolet_training, isolet_testing, cl, k=2, prob=TRUE)
prob <- attr(knn_isolet, "prob")

# However, they come on a form that ROCR does not accept so we need to invert them for 
# the -1 class and rescale them.
prob <- 2*ifelse(knn_isolet == "-1", 1-prob, prob) - 1


pred_knn <- prediction(prob, cl_testing)
pred_knn <- performance(pred_knn, "tpr", "fpr")
plot(pred_knn, avg= "threshold", colorize=T, lwd=3, main="a ROC curve!")