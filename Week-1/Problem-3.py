import pandas as pd
import numpy as np

names = ['Arjun', 'Babar', 'Chris Gayle', 'David Warner', 'Ellyse Perry', 'Henry', 'Kane Mama', 'Kohli', 'Smith' , 'Root']
subjects = ['Maths', 'Physics', 'Chemistry', 'Biology', 'Maths', 'Physics', 'Chemistry', 'Biology', 'Maths', 'Physics']

scores = np.random.randint(50, 101, size=10)
grades = [''] * 10  # Empty initially

df = pd.DataFrame({
    'Name': names,
    'Subject': subjects,
    'Score': scores,
    'Grade': grades
})

def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

df['Grade'] = df['Score'].apply(assign_grade)

print("DataFrame with Grades:")
print(df)

print("Sorted by Score (Descending):")
print(df.sort_values('Score', ascending=False))

print("Average Score for each Subject:")
print(df.groupby('Subject')['Score'].mean())

def pandas_filter_pass(dataframe):
    return dataframe[dataframe['Grade'].isin(['A', 'B'])]

print("Students with Grade 'A' or 'B':")
print(pandas_filter_pass(df))
