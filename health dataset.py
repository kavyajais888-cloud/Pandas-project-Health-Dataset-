import pandas as pd
import numpy as np

# Sample dataset
data = {
    'age': [22, 35, 47, 52, 29, 41, 38, 26, 33, 49],
    'weight': [60, 75, 82, 90, 68, 80, 72, 58, 70, 85],
    'height': [165, 175, 168, 180, 160, 172, 170, 158, 165, 177],
    'exercise': ['low', 'medium', 'high', 'medium', 'low', 'high', 'medium', 'low', 'high', 'medium'],
    'sleep': [6.5, 7.2, 5.5, 8.1, 7.5, 6.8, 5.9, 7.0, 6.3, 7.8],
    'sugar_intake': [40, 30, 50, 20, 35, 25, 30, 45, 38, 28],
    'smoking': [1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    'alcohol': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    'married': [0, 1, 1, 1, 0, 1, 1, 0, 1, 1],
    'profession': ['student', 'teacher', 'manager', 'engineer', 'nurse', 'lawyer', 'teacher', 'student', 'manager', 'doctor'],
}

df = pd.DataFrame(data)
# Compute BMI
df['bmi'] = df['weight'] / ((df['height'] / 100) ** 2)
# Health risk category based on BMI
df['health_risk'] = pd.cut(df['bmi'], bins=[0,18.5,25,30,100],
                           labels=['low','medium','high','very_high'])

# df.head()

# # 1. Display first 10 rows
# print(df.head(10))

# # 2. Show shape, dtypes, and memory usage
# print(df.shape)
# print(df.dtypes)
# print(df.info())

# # 3. Count missing values
# print(df.isnull().sum())

# # 4. Verify BMI formula
# df['BMI_check'] = df['weight'] / ((df['height'] / 100) ** 2)
# df['BMI_diff'] = abs(df['BMI_check'] - df['bmi'])
# flag_rows = df[df['BMI_diff'] > 0.2]
# print(flag_rows)

# 5. Clip sleep values and count clipped
# df['sleep'] = df['sleep'].clip(0, 24)
# print("Sleep values clipped count:", (df['sleep'] < 0).sum() + (df['sleep'] > 24).sum())

# 6. Count non-smokers with medium/high exercise and no alcohol
# non_smokers = df[(df['smoking'] == 0) & (df['exercise'].isin(['medium','high'])) & (df['alcohol'] == 0)]
# print("Count:", len(non_smokers))

# # 7. Among people sleeping ≥7 hours, average BMI by exercise
# print(df[df['sleep'] >= 7].groupby('exercise')['bmi'].mean())

# # 8. Median sleep & IQR by profession
# iqr_sleep = df.groupby('profession')['sleep'].agg(['median', lambda x: x.quantile(0.75) - x.quantile(0.25)])
# print(iqr_sleep)

# # 9. Top 5 professions by share of high health risk
# high_risk_share = (df['health_risk'] == 'high').groupby(df['profession']).mean().sort_values(ascending=False)
# print(high_risk_share.head(5))

# # 10. Create age bins
# bins = [0,25,34,44,54,100]
# labels = ['<25','25–34','35–44','45–54','55+']
# df['age_bin'] = pd.cut(df['age'], bins=bins, labels=labels)
# print(df.groupby('age_bin').agg({'bmi':'mean','smoking':'mean'}))


# # 11. Smoking × Alcohol table
# print(pd.crosstab(df['smoking'], df['alcohol'], margins=True, normalize='index'))

# # 12. % distribution of exercise levels per profession
# print(pd.crosstab(df['profession'], df['exercise'], normalize='index') * 100)

# # 13. Pivot table: mean sleep by exercise & sugar intake (categorized)
# df['sugar_cat'] = pd.cut(df['sugar_intake'], bins=[0,30,40,60], labels=['low','medium','high'])
# print(df.pivot_table(values='sleep', index='exercise', columns='sugar_cat', aggfunc='mean'))

# # 14. Relative risk of high health risk for smokers vs non-smokers
# risk_table = df.groupby('smoking')['health_risk'].value_counts(normalize=True).unstack()
# print(risk_table)

# # 15. For each exercise level, profession with lowest mean BMI
# lowest_bmi = df.groupby(['exercise','profession'])['bmi'].mean().reset_index()
# print(lowest_bmi.loc[lowest_bmi.groupby('exercise')['bmi'].idxmin()])

