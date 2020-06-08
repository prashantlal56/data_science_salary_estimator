import pandas as pd

X_test = pd.read_csv('X_test.csv')
#data_in =X_test.iloc[1,:].ravel()
data_in = pd.DataFrame(X_test.iloc[1,:].ravel().reshape(1,23),
 					   columns = X_test.columns.to_list())