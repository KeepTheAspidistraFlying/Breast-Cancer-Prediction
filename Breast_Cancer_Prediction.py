import pandas as pd
from sklearn.datasets import load_breast_cancer
cancer_data=load_breast_cancer();
print(cancer_data['DESCR']);
#as u can see there are 569 datapoints and 30 attributes.
#the target is either "Malignant" or "Benign" (Malignant=cancerous, Benign=not cancerous)
print(cancer_data['data'].shape);
#as u can see its a numpy array 569 rows and 30 columns.
print(cancer_data['feature_names']);
#its easier to work with columns that have names, so we bulid a dataframe with the name of "df"
#then changed the names of the columns to our dataset's features.
#(u can check the names of columns before changing were 0 to 29)
#we need a target column, u can also see the names of targets by printing cancer_data['target_names'];
#it will print malignant and benign.(mal=0 and ben=1)
df=pd.DataFrame(cancer_data['data'],columns=cancer_data['feature_names']);
df['target']=cancer_data['target'];
print(df.head());
#head method is used to show us a few first rows of the dataframe.(we can see the names of the columns on top)
#we need to make matrix X and array Y for logistic regression model.
X=df[cancer_data.feature_names].values;
Y=df['target'].values;
from sklearn.linear_model import LogisticRegression;
model=LogisticRegression(solver='liblinear');
model.fit(X,Y);
print(model.score(X,Y));
#just an example:
print(model.predict([[1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,11,1]]));