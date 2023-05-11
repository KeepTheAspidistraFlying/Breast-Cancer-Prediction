# Breast-Cancer-Prediction
Using Machine Learning/ Logistic Regression

Hey Guyz

so basically this project is the same as Titanic Survival Prediction, but I used a few different things here.

for basic info read Basics of Machine Learning in my repos.

so, in this project, I used one of datasets of sklearn. It contains 30 keys which are our attributes and 569 datapoints.
if ure interested in knowing why we use these features and how can we use more features, search "feature engineering".

the target is either Malignant or Benign (Malignant=cancerous, Benign=not cancerous)

So its easy to guess its "classification" and "supervised learning".
as explained before, we can use "logistic regression" algorithm for classification problems.
(again, dont mix the name of the algorithm with type of the problem it is used for.)

if u look at line 22 of the code, u can see the difference between this one and Titanic. u can write the method used in titanic and ull see that a warning arises stating:

STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.

there are 2 ways to solve this problem, u can increase the number of iterations or u can use other solvers. (as I did)

other solvers in Logistic Regression:

https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

u can see the accuracy is around 96%. u can also give the program ur 30 attributes and it will predict if its cancerous or not.
