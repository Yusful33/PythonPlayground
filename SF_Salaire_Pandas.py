import pandas as pd
sal = pd.read_csv('/Users/ycatttaneo/Documents/Data4Scripts/sf-salaries/Salaries.csv/Salaries.csv', low_memory=False)
print(sal.head())
#Checking data types in the file
print(sal.dtypes)
#This gives you the col names in a df
list(sal)
#Changing data types for one column
sal['BasePay'] = pd.to_numeric(sal['BasePay'], errors='coerce')
sal['OvertimePay'] = pd.to_numeric(sal['OvertimePay'], errors='coerce')
sal['OtherPay'] = pd.to_numeric(sal['OtherPay'], errors='coerce')
#Testing
sal.dtypes
sal['BasePay'].max()
joseph_driscoll = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']
joseph_driscoll['JobTitle']
joseph_driscoll['TotalPayBenefits']
#.loc allow you to earch on a particular row/column
#idxmax pulls the highest value
highest_paid = sal.loc[sal['TotalPayBenefits'].idxmax()]
highest_paid['EmployeeName']
lowest_paid = sal.loc[sal['TotalPayBenefits'].idxmin()]
lowest_paid
#avg BasePay of all employees per year
sal.groupby('Year').mean()['BasePay']
#Uniue Job Title
sal['JobTitle'].nunique()
#Ten most common jobs
sal['JobTitle'].value_counts().head(10)
#Job Title that were represented by only one person in 2013
sum(sal[sal['Year']==2013]['JobTitle'].value_counts()==1)
#People who have the name Chief in their job title
def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False
sum(sal['JobTitle'].apply(lambda x:chief_string(x)))
#Correlation between length of the Job Title String and Salary
sal['title_len'] = sal['JobTitle'].apply(len)
sal[['TotalPayBenefits', 'title_len']].corr()

#Correlation between all numerial variables
factors_paired = [(i,j)]