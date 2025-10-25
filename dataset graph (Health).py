import pandas as pd
import matplotlib.pyplot as plt

# Create sample health dataset
data = {
    'Name': ['Aarav', 'Diya', 'Rohan', 'Sneha', 'Vikram', 'Isha', 'Karan', 'Meera', 'Raj', 'Tina'],
    'Age': [25, 30, 28, 35, 40, 26, 33, 31, 29, 27],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Height_cm': [172, 160, 178, 155, 182, 165, 175, 162, 180, 158],
    'Weight_kg': [70, 55, 80, 50, 90, 52, 78, 56, 85, 54],
    'Blood_Pressure': [120, 110, 130, 115, 140, 108, 128, 112, 135, 110],
    'Cholesterol': [190, 160, 210, 175, 220, 165, 200, 170, 215, 180]
}

df = pd.DataFrame(data)
print(df)

# Q1. Display first 5 rows of the dataset.
df.head()

# Show the summary statistics of the dataset.
df.describe()

# Q3. Find the average (mean) weight of all people.
df['Weight_kg'].mean()

# Q4. Find the person with the highest cholesterol level.
df[df['Cholesterol'] == df['Cholesterol'].max()]

# Q5. Find how many males and females are there.
df['Gender'].value_counts()

# Q6. Add a new column for BMI (Body Mass Index).

df['BMI'] = df['Weight_kg'] / (df['Height_cm']/100)**2
df

# Q7. Find the person with BMI greater than 25 (Overweight).
df[df['BMI'] > 25]


# Q8. Sort the dataset by Age (ascending).
df.sort_values(by='Age')

# Q9. Group by Gender and find average weight.
df.groupby('Gender')['Weight_kg'].mean()

# Q10. Find correlation between Weight, Height, and Cholesterol.
df[['Weight_kg', 'Height_cm', 'Cholesterol']].corr()

# Q11. Plot a bar graph showing Age vs Weight.
plt.bar(df['Name'], df['Weight_kg'], color='skyblue')
plt.xlabel('Name')
plt.ylabel('Weight (kg)')
plt.title('Age vs Weight')
plt.xticks(rotation=45)
plt.show()

# Q12. Plot a histogram of BMI values.
plt.hist(df['BMI'], bins=5, color='lightgreen', edgecolor='black')
plt.xlabel('BMI')
plt.ylabel('Count')
plt.title('BMI Distribution')
plt.show()

# Q13. Plot a line graph showing Cholesterol vs Age.
plt.plot(df['Age'], df['Cholesterol'], marker='o', color='purple')
plt.xlabel('Age')
plt.ylabel('Cholesterol')
plt.title('Cholesterol Level vs Age')
plt.show()

# Q14. Show gender-wise average cholesterol using a bar chart.
avg_chol = df.groupby('Gender')['Cholesterol'].mean()
avg_chol.plot(kind='bar', color=['pink', 'lightblue'])
plt.title('Average Cholesterol by Gender')
plt.ylabel('Cholesterol')
plt.show()

# Q15. Scatter plot of Height vs Weight.
plt.scatter(df['Height_cm'], df['Weight_kg'], color='orange')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Height vs Weight')
plt.show()



