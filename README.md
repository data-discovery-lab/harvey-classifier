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

###### accuracy:  0.93 ; precision:  0.605263157894737 ; recall:  0.793103448275862 ; f-measure:  0.686567164179104







### ROC Curves

![KNN-1-5](https://github.com/litpuvn/harvey-classifier/raw/master/r/knn-1-5.png)

## SVM using LibShortText Library

LibShortText Library is already forked in this project. To begin, you must be using a Linux based machine. Change your directory to the libshort folder and run the command 'make'. After these steps are completed you are now ready to to use LibShortText.

**Link to Libshort Folder:** https://github.com/litpuvn/harvey-classifier/tree/master/libshorttext-1.1

**Required OS:** Linux

**Terminal Command Required:** `$ make`

### Basic SVM Accuracy Prediction

In order to us LibShortText through the terminal be sure to format the data as described below. Once that is done, you are able to us the library from the terminal.

**Text File Format (.txt):** <LABEL><TAB><TEXT>
```
1    harveyrescue harveyrelief eliza(832) 25742376506 glenmorris crt houston77084
1    harveyrescue harveyrelief urgent alone elderly woman11611 innsbury(btwn bertrand hopper in aldine) houston 77093 flooded home
1    harveyrescue harveyrelief one adult disable (sickle cell anemia) sharon beverly 10126 valley club dr houston tx 77078
0    sosharveyrescue strandedhouston uscg billbishopkhou houstonpolice nationalguard texasguard cohoustonfire amodm9onf3
0    love this look for the helpers you will always find people who are helping harvey2017 prayfortexas khtgfvkfer
0    text harvey to 90999 help our friends in texas esqvx9sbg4
```
  
**Train Text File:**

Train a properly formatted text file to obtain a model. This process will generate a train_file.model folder that will be used to help predict results

```
$ python text-train.py train-rescue-500.txt
[output information]
```

**Predict Results:**

Predicts the results of the test file using the trained model that was generated from above. The output of this command is an accuracy precentage of how well the model processed the test file.

```
$ python text-predict.py text-rescue-500.txt train-rescue-500.txt.model predict_result
Accuracy = 87.4627% (293/335)
```

**Full Terminal Example:**

![SVM-Accuracy-Example](https://github.com/litpuvn/harvey-classifier/blob/master/libshorttext-1.1/Rescue-SVM-Demo/SVM_Accuracy_Ex.png)


