## A set of classifiers to study Harvey data set

Supported Classifiers:

#### KNN - Studied K=1-5 and found k =1 has the best f-measure as our data is skew (more none-rescue than rescue data)


###### k = 1 accuracy= 92.6  p = 1 r = 0.412698412698413 f-measure = 0.584269662921348

###### k = 2 accuracy= 91  p = 1 r = 0.285714285714286 f-measure = 0.444444444444444

###### k = 3 accuracy= 90.2  p = 1 r = 0.222222222222222 f-measure = 0.363636363636364

###### k = 4 accuracy= 90  p = 1 r = 0.206349206349206 f-measure = 0.342105263157895

###### k = 5 accuracy= 88.6  p = 1 r = 0.0952380952380952 f-measure = 0.173913043478261

#### CART - model

###### accuracy = 0.916666666666667 , p = 0.709677419354839 r = 0.578947368421053  f-measure = 0.63768115942029


#### Logistic regression

###### accuracy:  0.703333333333333 ; precision:  0.247524752475248 ; recall:  0.657894736842105 ; f-measure:  0.359712230215827

### SVM - RTextTools

#####                                precision: 0.865 ; recall: 0.795 ; f-measure: 0.825






### ROC Curves

![KNN-1-5](https://github.com/litpuvn/harvey-classifier/raw/master/r/knn-1-5.png)

