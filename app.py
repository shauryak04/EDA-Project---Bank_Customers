import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("bank_customers.csv")
df.head()
print(df.describe())
print(df.info())

df.isnull().sum()
df.duplicated().sum()
#univariate analysis

df['Age'].hist()
plt.title("Age Distribution")
plt.show()

df['Gender'].value_counts()
df['Gender'].value_counts().plot(kind="bar")
plt.title("Gender Distribution")
plt.show()

df['AccountType'].value_counts().plot(kind="pie",autopct='%1.1f%%')
plt.title("Savings vs Current")
plt.show()

sns.boxplot(df['Income'])
plt.title("income distribution")
plt.show()

sns.scatterplot(data=df,x='Balance',y='CreditScore')
plt.title("Balance vs Credit")
plt.show()

sns.boxplot(data=df,x='LoanStatus',y='Income')
plt.title("LoanStaus by income")
plt.show()

sns.boxplot(data=df,x='LoanStatus',y='CreditScore')
plt.title("LoanStatus by CreditScore")
plt.show()

sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

df.groupby("City")["Income"].mean().plot(kind="bar")
plt.title("Average Income per City")
plt.show()
