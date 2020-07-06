"""
    This is an illustration of covariance and correlation analysis


"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('max_columns', None)
pd.set_option("max_rows", None)

#load dataset
df = pd.read_csv("../data/diabetes.csv").dropna()
# data info
#print(df.describe())

df_filter = df[(df.Outcome == 1)]
#print(df_filter)

cov_mat = df_filter.cov()
corr_mat = df_filter.corr()

sns.heatmap(corr_mat, annot=True)
plt.show()