import pandas as pd
df = pd.read_csv('tackoverflow_qa.csv')
df.head()
df['creationdate'] = pd.to_datetime(df['creationdate'])
df_filtered = df[df['creationdate'].dt.year>2014]
df_filtered
df_score50 = df[df['score']>50]
df_score50
df_score_between = df[df['score'].between(50,100)]
df_score_between
df_Scott = df[df['ans_name']=='Scott Boston']
df_Scott
top_users = df['ans_name'].value_counts().head(5).index.tolist()
top_users
filtered = df[df['ans_name'].isin(top_users)]
filtered
print(filtered[['id', 'title', 'ans_name']])
df['creationdate'] = pd.to_datetime(df['creationdate'])
filtered_by_date = df[
    df['creationdate'].between('2014-03-01', '2014-10-31') & 
    (df['ans_name'].fillna('').str.lower()=='unutbu') & 
    (df['score']<5)
    ]
filtered_by_date
filtered_by_or = df[df['score'].between(5,10) |(df['viewcount']>10000)]
filtered_by_or[['id','creationdate','score','viewcount']]
df[(df['ans_name'].notna())&(df['ans_name'] != 'Scott Boston')]

titanic_df1 = pd.read_csv('titanic.csv')
titanic_df1.head()
titanic_df1[(titanic_df1['Sex'].str.lower()=='female')&(titanic_df1['Age'].between(20,30))]
Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.
filter_by_paid_passenger = titanic_df1[titanic_df1['Fare']>100]
filter_by_paid_passenger
Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).
sort_by_survived_nosibsp = titanic_df1[(titanic_df1['Survived'])&(titanic_df1['SibSp']==0)]
sort_by_survived_nosibsp
Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.
filter_by_C_Fare = titanic_df1[(titanic_df1['Embarked']=='C')&(titanic_df1['Fare']>50)]
filter_by_C_Fare
titanic_df1[(titanic_df1['SibSp']==2) & (titanic_df1['Parch']==2)]
filter_by_age = titanic_df1[(titanic_df1['Age']<=15)&(titanic_df1['Survived']==0)]
filter_by_age
titanic_df1[(titanic_df1['Fare']>200)&(titanic_df1['Cabin'].notna())]
sorted_by_odd_id = titanic_df1[titanic_df1['PassengerId']%2==1 ]
sorted_by_odd_id
ticket_counts = titanic_df1['Ticket'].value_counts()
unique_ticket_values = ticket_counts[ticket_counts==1].index
unique_tickets_titanic = titanic_df1[titanic_df1['Ticket'].isin(unique_ticket_values)]
unique_tickets_titanic
female_passangers = titanic_df1[(titanic_df1['Sex'].str.lower()=='female')&(titanic_df1['Pclass']==1)]
has_Miss_in_name = female_passangers[female_passangers['Name'].str.contains('Miss')]
has_Miss_in_name
















